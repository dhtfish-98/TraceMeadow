"""Owned wire data and actual EOF/resource/read boundaries, independent of parser internals."""
from dataclasses import replace
from io import BytesIO
from pathlib import Path
import ast
import os
import plistlib
import struct
import subprocess
import sys
import pytest
from click.testing import CliRunner
from tracemeadow.binary_stream import meadow_KdBufParser, meadow_seek_until
from tracemeadow.bounded_stream import MeadowLimits, MeadowReader, TraceFormatError, meadow_checked_plist
from tracemeadow.console import meadow_cli, meadow_print_with_count
import tracemeadow.console as console

ROOT = Path(__file__).resolve().parents[1]
V2 = b'\x00\x02\xaaU'
V3 = b'\x00\x03\xaaU'
STACK = b'stackshot_out_fl'
THREADS = b'\x00\x1d\x00\x00\0\0\0\0'
EVENTS = b'\x00\x1e\x00\x00\0\0\0\0'
MORE = b'\x00\x20\x00\x00\0\0\0\0'
TAGS = dict(dyld=b'\x01\x80\0\0\0\0\0\0', codes=b'\x0f\x80\0\0\0\0\0\0',
            processes=b'\x10\x80\0\0\0\0\0\0', logs=b'\x11\x80\0\0\0\0\0\0',
            strings=b'\x12\x80\0\0\0\0\0\0', kexts=b'\x05\x80\0\0\0\0\0\0',
            images=b'\x04\x80\0\0\x01\0\0\0')


def record(timestamp=256, tid=42, debug=0x040C0002):
    return struct.pack('<Q4QQIIQ', timestamp, 1, 2, 3, 4, tid, debug, 0, 0)


def thread(tid=42, pid=7, name=b'OwnedProcess\0'):
    return struct.pack('<QI20s', tid, pid, name)


def v2(records=None, padding=0, threads=()):
    header = struct.pack('<I', len(threads)) + bytes(280)
    return V2 + header + b''.join(threads) + bytes(padding) + b''.join(records if records is not None else [record()])


def v3_prefix(threads=()):
    cpu = plistlib.dumps({'CPUCount': 1}, fmt=plistlib.FMT_BINARY)
    header = struct.pack('<IIQIIQQIIIIIQ', 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, len(cpu)) + cpu
    return V3 + header + bytes((-len(header)) % 8) + bytes(4) + STACK + THREADS + struct.pack('<Q', len(threads)*32) + b''.join(threads)


def event_chunk(records, includes_prefix=False):
    return EVENTS + struct.pack('<Q', len(records)*64 + (8 if includes_prefix else 0)) + bytes(8) + b''.join(records)


def metadata(tag, value, aligned=True):
    data = value if isinstance(value, bytes) else plistlib.dumps(value, fmt=plistlib.FMT_BINARY)
    return tag + struct.pack('<Q', len(data)) + data + (bytes((-len(data)) % 8) if aligned else b'')


def parse(data, **options):
    parser = meadow_KdBufParser(**options)
    events = list(parser.meadow_parse(BytesIO(data)))
    return parser, events


@pytest.mark.parametrize('timestamp', [0, 1, 256, 65536, 2**64-1])
def test_v2_zero_prefix_is_event_data(timestamp):
    parser, events = parse(v2([record(timestamp)], threads=[thread()]))
    assert len(events)==1 and events[0].timestamp==timestamp and events[0].values==(1,2,3,4)
    assert parser.threads_pids=={42:7} and parser.pids_names=={7:'OwnedProcess'}


@pytest.mark.parametrize('padding', [0, 1, 32, 64, 3808, 4096])
def test_v2_explicit_padding(padding):
    _, events = parse(v2([record(0)], padding), v2_padding=padding)
    assert len(events)==1 and events[0].timestamp==0


@pytest.mark.parametrize('size', list(range(1,64)))
def test_v2_rejects_truncated_final_record(size):
    with pytest.raises(TraceFormatError, match='truncated'):
        parse(v2([record()[:size]]))


@pytest.mark.parametrize('cut', range(len(v3_prefix()+event_chunk([record()]))))
def test_v3_eof_at_each_required_byte(cut):
    with pytest.raises(TraceFormatError):
        parse((v3_prefix()+event_chunk([record()]))[:cut])


@pytest.mark.parametrize('includes_prefix', [False,True])
def test_v3_multiple_chunks_and_all_metadata(includes_prefix):
    data = v3_prefix([thread()]) + event_chunk([record(1)], includes_prefix) + MORE + event_chunk([record(2)], includes_prefix)
    data += metadata(TAGS['dyld'], {'Binaries':[{'Name':'OwnedImage'}], 'Other':1})
    data += metadata(TAGS['dyld'], {'Binaries':[{'Name':'OwnedImage2'}]})
    data += metadata(TAGS['kexts'], {'Binaries':[{'Name':'OwnedKext'}]})
    data += metadata(TAGS['processes'], {'Processes':[{'PID':7}]})
    data += metadata(TAGS['images'], {'OwnedImage':{'Address':1}})
    data += metadata(TAGS['codes'], b'040c0000 OWNED_EVENT\n')
    data += metadata(b'unknown!', b'ignored')
    parser, events = parse(data)
    assert [e.timestamp for e in events]==[1,2]
    assert parser.v3_header.timebase_numer==1 and parser.v3_header.cpu_info=={'CPUCount':1}
    assert parser.dyld_modules=={'Binaries':[{'Name':'OwnedImage'},{'Name':'OwnedImage2'}],'Other':1}
    assert parser.kernel_extensions=={'Binaries':[{'Name':'OwnedKext'}]}
    assert parser.processes=={'Processes':[{'PID':7}]} and parser.images=={'OwnedImage':{'Address':1}}
    assert parser.trace_codes=='040c0000 OWNED_EVENT\n'


def test_v3_log_records_and_strings_retain_wire_values():
    # Existing attributed upstream fixtures provide the separately tested OS-log contract.
    tree=ast.parse((ROOT/'checks/test_meadow_os_log_event.py').read_text())
    case=next(n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name=='meadow_test_parsing_raw_log_event')
    values=[ast.literal_eval(n.value) for n in case.body if isinstance(n,ast.Assign) and isinstance(n.value,ast.Dict)]
    raw, strings=values[:2]
    data=v3_prefix()+event_chunk([])+metadata(TAGS['logs'], {'Events':[raw]})+metadata(TAGS['strings'], {'StringIndex':{k:v for v,k in strings.items()}})
    parser, events=parse(data)
    assert len(events)==1 and events[0].process=='locationd' and events[0].thread_identifier==2263
    assert events[0].composed_message==strings[2053] and parser.threads_pids[2263]==70


class Fragments:
    def __init__(self, data): self.data=BytesIO(data)
    def read(self, count): return self.data.read(min(count,3))


def test_fragmented_nonseekable_input_and_marker_pushback():
    data=v3_prefix()+event_chunk([record()])+metadata(TAGS['processes'], {'Processes':[]})
    parser=meadow_KdBufParser()
    assert len(list(parser.meadow_parse(Fragments(data))))==1
    stream=BytesIO(b'prefix-marker-tail')
    meadow_seek_until(stream,b'marker')
    assert stream.read()==b'-tail'
    bare=Fragments(b'prefix-marker-tail'); meadow_seek_until(bare,b'marker'); assert bare.data.read()==b'-tail'
    with pytest.raises(TraceFormatError,match='EOF'): meadow_seek_until(BytesIO(b'absent'),b'marker')
    with pytest.raises(TraceFormatError): meadow_seek_until(BytesIO(b''),b'')


def test_input_and_search_limits_are_actual_work_bounds():
    with pytest.raises(TraceFormatError,match='input byte limit'):
        parse(v2(), limits=replace(MeadowLimits(),input_bytes=300))
    reader=MeadowReader(BytesIO(b'X'*20),replace(MeadowLimits(),search_bytes=8))
    with pytest.raises(TraceFormatError,match='search limit'):reader.marker(b'missing')
    assert reader.received==8


@pytest.mark.parametrize('limit', ['threads','events','blocks','block_bytes'])
def test_declared_count_and_chunk_limits(limit):
    value={'threads':1,'events':1,'blocks':1,'block_bytes':96}[limit]
    limits=replace(MeadowLimits(),**{limit:value})
    if limit=='threads':data=v2(threads=[thread(1),thread(2)])
    elif limit=='events':data=v2([record(),record()])
    elif limit=='blocks':data=v3_prefix()+event_chunk([])+metadata(TAGS['codes'],b'x')
    else:data=v3_prefix()+event_chunk([record(),record()])
    with pytest.raises(TraceFormatError):parse(data,limits=limits)


def test_duplicate_threads_and_unterminated_names_are_rejected():
    for data in [v2(threads=[thread(),thread()]),v2(threads=[thread(name=b'A'*20)])]:
        with pytest.raises(TraceFormatError):parse(data)
    with pytest.raises(TraceFormatError,match='padding'):
        parse(V2+bytes(284)+b'X'+record(),v2_padding=1)


@pytest.mark.parametrize('fmt',[plistlib.FMT_XML,plistlib.FMT_BINARY])
def test_plist_depth_and_allocation_limits(fmt):
    value={}; cursor=value
    for _ in range(20):cursor['child']={};cursor=cursor['child']
    with pytest.raises(TraceFormatError):meadow_checked_plist(plistlib.dumps(value,fmt=fmt),replace(MeadowLimits(),metadata_depth=8))
    with pytest.raises(TraceFormatError):meadow_checked_plist(plistlib.dumps({'items':list(range(100))},fmt=fmt),replace(MeadowLimits(),metadata_nodes=10))


def test_plist_cycles_duplicates_entities_and_invalid_metadata():
    cycle=[];cycle.append(cycle)
    with pytest.raises(TraceFormatError,match='cyclic'):meadow_checked_plist(plistlib.dumps(cycle,fmt=plistlib.FMT_BINARY),MeadowLimits())
    xml=b'<plist><dict><key>a</key><integer>1</integer><key>a</key><integer>2</integer></dict></plist>'
    with pytest.raises(TraceFormatError,match='duplicate'):meadow_checked_plist(xml,MeadowLimits())
    xml=b'<!DOCTYPE plist [<!ENTITY x "value">]><plist><string>&x;</string></plist>'
    with pytest.raises(TraceFormatError,match='entity'):meadow_checked_plist(xml,MeadowLimits())
    for tag,value in [(TAGS['logs'],{'Events':{}}),(TAGS['kexts'],{'Binaries':{}}),(TAGS['strings'],{'StringIndex':{'a':1,'b':1}}),(TAGS['images'],['wrong'])]:
        with pytest.raises(TraceFormatError):parse(v3_prefix()+event_chunk([])+metadata(tag,value))


def test_truncated_additional_payload_is_not_silently_ignored():
    prefix=v3_prefix()+event_chunk([])
    block=metadata(TAGS['processes'],{'Processes':[]})
    payload_size=struct.unpack_from('<Q',block,8)[0]
    for cut in range(1,16+payload_size):
        with pytest.raises(TraceFormatError):parse(prefix+block[:cut])
    # A final unaligned metadata block remains compatible with the historical dialect.
    parser,_=parse(prefix+metadata(TAGS['processes'],{'Processes':[]},aligned=False))
    assert parser.processes=={'Processes':[]}


def test_count_consumes_no_extra_record_and_output_is_bounded(monkeypatch,capsys):
    consumed=[]
    def sequence():
        for i in range(3):consumed.append(i);yield i
    meadow_print_with_count(sequence(),0);assert not consumed
    meadow_print_with_count(sequence(),1);assert consumed==[0]
    monkeypatch.setattr(console,'meadow_OUTPUT_LIMIT',3)
    with pytest.raises(TraceFormatError,match='output byte limit'):meadow_print_with_count(iter(['long']),-1)
    assert capsys.readouterr().out=='0\n'


def test_cli_errors_padding_stdin_and_metadata_drain(tmp_path):
    owned=tmp_path/'owned';owned.write_bytes(v2([record(0)],32));digest=owned.read_bytes()
    done=CliRunner().invoke(meadow_cli,['--v2-padding','32','kevents',str(owned)])
    assert done.exit_code==0 and 'Owned' not in done.output and '0x40c0000' in done.output.lower()
    for command in ['processes','images','kexts']:
        done=CliRunner().invoke(meadow_cli,['--v2-padding','32',command,str(owned)])
        assert done.exit_code==0
    done=CliRunner().invoke(meadow_cli,['kevents','-'],input=v2([record()]))
    assert done.exit_code==0
    done=CliRunner().invoke(meadow_cli,['kevents',str(owned),'-c','-2'])
    assert done.exit_code==2
    owned.write_bytes(b'bad')
    done=CliRunner().invoke(meadow_cli,['kevents',str(owned)])
    assert done.exit_code==2 and 'truncated' in done.output and 'Traceback' not in done.output
    owned.write_bytes(digest)
    assert {p.name for p in tmp_path.iterdir()}=={'owned'}


def test_cli_no_fifo_or_symlink_hang_and_no_missing_marker_loop(tmp_path):
    owned=tmp_path/'owned';owned.write_bytes(v3_prefix())
    link=tmp_path/'link';link.symlink_to(owned)
    fifo=tmp_path/'fifo';os.mkfifo(fifo)
    for path in [owned,link,fifo,tmp_path]:
        done=subprocess.run([sys.executable,'-m','tracemeadow.console','kevents',str(path)],capture_output=True,timeout=3,
                            env={**os.environ,'PYTHONPATH':str(ROOT/'src')})
        assert done.returncode==2 and b'Traceback' not in done.stderr
    assert owned.read_bytes()==v3_prefix() and {p.name for p in tmp_path.iterdir()}=={'owned','link','fifo'}


def test_binary_plist_duplicate_keys_and_preallocation_limit(monkeypatch):
    objects=b'\xd2\x01\x01\x02\x03\x51a\x10\x01\x10\x02'
    table=8+len(objects)
    duplicate=b'bplist00'+objects+bytes([8,13,15,17])+bytes(6)+bytes([1,1])+struct.pack('>3Q',4,0,table)
    assert plistlib.loads(duplicate)=={'a':2}
    with pytest.raises(TraceFormatError):
        meadow_checked_plist(duplicate,MeadowLimits())
    objects=b'\xaf\x12'+struct.pack('>I',1000)+b'\x01'*1000+b'\x00'
    table=8+len(objects)
    oversized=b'bplist00'+objects+struct.pack('>2H',8,8+len(objects)-1)+bytes(6)+bytes([2,1])+struct.pack('>3Q',2,0,table)
    assert plistlib.loads(oversized)==[None]*1000
    def forbidden_load(*args,**kwargs):raise AssertionError('oversized object must be rejected before plist decoding')
    monkeypatch.setattr(plistlib,'loads',forbidden_load)
    with pytest.raises(TraceFormatError,match='reference limit'):
        meadow_checked_plist(oversized,replace(MeadowLimits(),metadata_nodes=10))


def test_cli_json_preserves_binary_and_date_values(tmp_path):
    import datetime,json
    value={'UUID':b'\0\xff','When':datetime.datetime(2026,1,1),'Index':plistlib.UID(7)}
    owned=tmp_path/'owned';owned.write_bytes(v3_prefix()+event_chunk([])+metadata(TAGS['images'],value))
    result=CliRunner().invoke(meadow_cli,['images',str(owned)])
    assert result.exit_code==0
    assert json.loads(result.output)=={'UUID':{'$bytes_hex':'00ff'},'When':{'$datetime':'2026-01-01T00:00:00'},'Index':{'$plist_uid':7}}


def test_cumulative_metadata_and_detectable_input_changes(tmp_path):
    data=v3_prefix()+event_chunk([])+metadata(TAGS['processes'],{'Processes':[]})+metadata(TAGS['images'],{'Images':[]})
    with pytest.raises(TraceFormatError,match='cumulative'):
        parse(data,limits=replace(MeadowLimits(),block_bytes=128))
    owned=tmp_path/'owned';owned.write_bytes(v2())
    with owned.open('rb') as raw:
        wrapper=console.MeadowLocalFile(raw,os.fstat(raw.fileno()))
        assert wrapper.read(4)==V2
        with owned.open('ab') as writer:writer.write(b'X')
        wrapper.read(4096)
        with pytest.raises(TraceFormatError,match='changed'):
            wrapper.read(1)

@pytest.mark.parametrize('text', ['onlyone', 'FFFFFFFFFFFFFFFF NAME', '-1 NAME', 'nothex NAME', '100000000 NAME'])
def test_trace_code_text_rejects_invalid_wire_identifiers(text):
    from tracemeadow.code_index import meadow_from_trace_codes_text
    with pytest.raises(TraceFormatError): meadow_from_trace_codes_text(text)


def test_trace_code_catalog_aliases_and_bounded_file_input(tmp_path,monkeypatch):
    import tracemeadow.code_index as codes
    assert codes.from_trace_codes_text('00000001 OLD\n\n00000001 NEW\n')=={1:'NEW'}
    owned=tmp_path/'codes';owned.write_bytes(b'00000001 OWNED\n')
    assert codes.from_trace_codes_file(owned)=={1:'OWNED'}
    link=tmp_path/'link';link.symlink_to(owned)
    with pytest.raises(OSError):codes.from_trace_codes_file(link)
    monkeypatch.setattr(codes,'meadow_CODE_BYTES',8)
    with pytest.raises(TraceFormatError):codes.from_trace_codes_file(owned)
