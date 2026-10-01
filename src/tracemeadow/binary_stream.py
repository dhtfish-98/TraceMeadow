# Derived from pykdebugparser/kd_buf_parser.py; original copyright and license in ORIGIN.md and LICENSE.
import tracemeadow_boundary as _name_boundary
import struct as meadow_struct
from collections import namedtuple as meadow_namedtuple
import io as meadow_io
import plistlib as meadow_plistlib
from construct import Adapter as meadow_Adapter, Struct as meadow_Struct, Const as meadow_Const, Padding as meadow_Padding, Int32ul as meadow_Int32ul, Int64ul as meadow_Int64ul, Array as meadow_Array, GreedyRange as meadow_GreedyRange, Byte as meadow_Byte, FixedSized as meadow_FixedSized, CString as meadow_CString, Prefixed as meadow_Prefixed, GreedyBytes as meadow_GreedyBytes, Aligned as meadow_Aligned, Bytes as meadow_Bytes, Select as meadow_Select
from tracemeadow.event_records import meadow_from_kd_buf as meadow_from_kd_buf, meadow_KD_BUF_FORMAT as meadow_KD_BUF_FORMAT
from tracemeadow.log_records import meadow_OsLogEvent as meadow_OsLogEvent
meadow_KEVENT_SIZE = meadow_struct.calcsize(meadow_KD_BUF_FORMAT)
meadow_ProcessData = _name_boundary.named_record('ProcessData', ['pid', 'name'])
meadow_RAW_VERSION_SIZE = 4
meadow_RAW_VERSION2_BYTES = b'\x00\x02\xaaU'
meadow_RAW_VERSION3_BYTES = b'\x00\x03\xaaU'
meadow_TRACEV3_STACKSHOT_END = b'stackshot_out_fl'
meadow_TRACEV3_THREADMAP_TAG = b'\x00\x1d\x00\x00\x00\x00\x00\x00'
meadow_TRACEV3_EVENTS_TAG = b'\x00\x1e\x00\x00\x00\x00\x00\x00'
meadow_TRACEV3_MORE_EVENTS = b'\x00 \x00\x00\x00\x00\x00\x00'
meadow_TRACEV3_DYLD_MODULES = b'\x01\x80\x00\x00\x00\x00\x00\x00'
meadow_TRACEV3_TRACE_CODES = b'\x0f\x80\x00\x00\x00\x00\x00\x00'
meadow_TRACEV3_PROCESSES = b'\x10\x80\x00\x00\x00\x00\x00\x00'
meadow_TRACEV3_LOG_EVENTS = b'\x11\x80\x00\x00\x00\x00\x00\x00'
meadow_TRACEV3_LOG_STRINGS = b'\x12\x80\x00\x00\x00\x00\x00\x00'
meadow_TRACEV3_KERNEL_EXTENSIONS = b'\x05\x80\x00\x00\x00\x00\x00\x00'
meadow_TRACEV3_IMAGES = b'\x04\x80\x00\x00\x01\x00\x00\x00'
meadow_kd_threadmap = meadow_Struct('tid' / meadow_Int64ul, 'pid' / meadow_Int32ul, 'process' / meadow_FixedSized(20, meadow_CString('utf8')))

@_name_boundary.class_contract('BplistAdapter', {})
class meadow_BplistAdapter(meadow_Adapter):
    """
    Construct adapter ti build and parse plists.
    """

    @_name_boundary.callable_contract({'self': 'meadow_self_5077f15', 'obj': 'meadow_obj_e0a635c', 'context': 'meadow_context_849b4ee', 'path': 'meadow_path_ded750f'}, '_decode')
    def _decode(meadow_self_5077f15, meadow_obj_e0a635c, meadow_context_849b4ee, meadow_path_ded750f):
        return meadow_plistlib.loads(meadow_obj_e0a635c)

    @_name_boundary.callable_contract({'self': 'meadow_self_675f428', 'obj': 'meadow_obj_7957e58', 'context': 'meadow_context_7e8133e', 'path': 'meadow_path_4a479b6'}, '_encode')
    def _encode(meadow_self_675f428, meadow_obj_7957e58, meadow_context_7e8133e, meadow_path_4a479b6):
        return meadow_plistlib.dumps(meadow_obj_7957e58)
meadow_kd_header_v2 = meadow_Struct('number_of_treads' / meadow_Int32ul, meadow_Padding(8), meadow_Padding(4), 'is_64bit' / meadow_Int32ul, 'tick_frequency' / meadow_Int64ul, meadow_Padding(256), 'threadmap' / meadow_Array(lambda meadow_ctx_90ee768: meadow_ctx_90ee768.number_of_treads, meadow_kd_threadmap), '_pad' / meadow_GreedyRange(meadow_Const(0, meadow_Byte)))
meadow_kd_header_v3 = meadow_Struct('tag' / meadow_Int32ul, 'sub_tag' / meadow_Int32ul, 'length' / meadow_Int64ul, 'timebase_numer' / meadow_Int32ul, 'timebase_denom' / meadow_Int32ul, 'timestamp' / meadow_Int64ul, 'walltime_secs' / meadow_Int64ul, 'walltime_usecs' / meadow_Int32ul, 'timezone_minuteswest' / meadow_Int32ul, 'timezone_dst' / meadow_Int32ul, 'flags' / meadow_Int32ul, 'tag2' / meadow_Int32ul, 'cpu_info' / meadow_Prefixed(meadow_Int64ul, meadow_BplistAdapter(meadow_GreedyBytes)))
meadow_kd_v3_threadmap = meadow_Struct('threadmap' / meadow_Prefixed(meadow_Int64ul, meadow_GreedyRange(meadow_kd_threadmap)))
meadow_kd_v3_additional_data = meadow_GreedyRange(meadow_Struct('tag' / meadow_Bytes(8), 'data' / meadow_Select(meadow_Aligned(8, meadow_Prefixed(meadow_Int64ul, meadow_GreedyBytes)), meadow_Prefixed(meadow_Int64ul, meadow_GreedyBytes))))

@_name_boundary.callable_contract({'reader': 'meadow_reader_99fe9e3', 'data': 'meadow_data_3dc4e15'}, 'seek_until')
def meadow_seek_until(meadow_reader_99fe9e3, meadow_data_3dc4e15: bytes):
    """
    Read from a stream until matching data.
    Reading is aligned to the data size.
    :param reader: Stream to read from.
    :param data: Data to match.
    """
    meadow_found_b4fe8c3 = meadow_reader_99fe9e3.read(len(meadow_data_3dc4e15))
    while meadow_found_b4fe8c3 != meadow_data_3dc4e15:
        meadow_found_b4fe8c3 = meadow_found_b4fe8c3[1:] + meadow_reader_99fe9e3.read(1)

@_name_boundary.class_contract('KdBufParser', {'parse': 'meadow_parse', 'set_thread_map': 'meadow_set_thread_map', 'parse_v2': 'meadow_parse_v2', 'parse_v3': 'meadow_parse_v3', 'threads_pids': 'meadow_threads_pids', 'pids_names': 'meadow_pids_names', 'versions': 'meadow_versions', 'trace_codes': 'meadow_trace_codes', 'images': 'meadow_images', 'dyld_modules': 'meadow_dyld_modules', 'processes': 'meadow_processes', 'kernel_extensions': 'meadow_kernel_extensions', 'v3_header': 'meadow_v3_header'})
class meadow_KdBufParser:
    """
    Parser for raw kd_buf buffer.
    """

    @_name_boundary.callable_contract({'self': 'meadow_self_41ba951', 'threads_pids': 'meadow_threads_pids_bdd884d', 'pids_names': 'meadow_pids_names_3faa2eb'}, '__init__')
    def __init__(meadow_self_41ba951, meadow_threads_pids_bdd884d=None, meadow_pids_names_3faa2eb=None):
        _name_boundary.attributes(meadow_self_41ba951)['threads_pids'] = {} if meadow_threads_pids_bdd884d is None else meadow_threads_pids_bdd884d
        _name_boundary.attributes(meadow_self_41ba951)['pids_names'] = {} if meadow_pids_names_3faa2eb is None else meadow_pids_names_3faa2eb
        _name_boundary.attributes(meadow_self_41ba951)['versions'] = {meadow_RAW_VERSION2_BYTES: _name_boundary.attributes(meadow_self_41ba951)['parse_v2'], meadow_RAW_VERSION3_BYTES: _name_boundary.attributes(meadow_self_41ba951)['parse_v3']}
        _name_boundary.attributes(meadow_self_41ba951)['trace_codes'] = ''
        _name_boundary.attributes(meadow_self_41ba951)['images'] = {}
        _name_boundary.attributes(meadow_self_41ba951)['dyld_modules'] = {}
        _name_boundary.attributes(meadow_self_41ba951)['processes'] = {}
        _name_boundary.attributes(meadow_self_41ba951)['kernel_extensions'] = {'Binaries': []}
        _name_boundary.attributes(meadow_self_41ba951)['v3_header'] = None

    @_name_boundary.callable_contract({'self': 'meadow_self_185ea55', 'reader': 'meadow_reader_1917485'}, 'parse')
    def meadow_parse(meadow_self_185ea55, meadow_reader_1917485: meadow_io.IOBase):
        """
        Parse kevents from a stream.
        :param reader: Stream to read from.
        :return: Generator for parsed kevents.
        """
        meadow_version_7a707ac = meadow_reader_1917485.read(meadow_RAW_VERSION_SIZE)
        return _name_boundary.attributes(meadow_self_185ea55)['versions'][meadow_version_7a707ac](meadow_reader_1917485)

    @_name_boundary.callable_contract({'self': 'meadow_self_201b121', 'parsed_threadmap': 'meadow_parsed_threadmap_5fa1966'}, 'set_thread_map')
    def meadow_set_thread_map(meadow_self_201b121, meadow_parsed_threadmap_5fa1966):
        _name_boundary.attributes(meadow_self_201b121)['threads_pids'].clear()
        _name_boundary.attributes(meadow_self_201b121)['pids_names'].clear()
        for meadow_thread_c6399dc in meadow_parsed_threadmap_5fa1966:
            _name_boundary.attributes(meadow_self_201b121)['threads_pids'][meadow_thread_c6399dc.tid] = meadow_thread_c6399dc.pid
            _name_boundary.attributes(meadow_self_201b121)['pids_names'][meadow_thread_c6399dc.pid] = meadow_thread_c6399dc.process

    @_name_boundary.callable_contract({'self': 'meadow_self_982bf42', 'reader': 'meadow_reader_befe2d1'}, 'parse_v2')
    def meadow_parse_v2(meadow_self_982bf42, meadow_reader_befe2d1: meadow_io.IOBase):
        """
        Parse trace version 2.
        :param reader: Stream to parse.
        :return: Generator for parsed kevents.
        """
        meadow_parsed_header_b98bf3e = meadow_kd_header_v2.parse_stream(meadow_reader_befe2d1)
        _name_boundary.attributes(meadow_self_982bf42)['set_thread_map'](meadow_parsed_header_b98bf3e.threadmap)
        while True:
            meadow_buf_f8120c4 = meadow_reader_befe2d1.read(meadow_KEVENT_SIZE)
            if not meadow_buf_f8120c4:
                break
            yield meadow_from_kd_buf(meadow_buf_f8120c4)

    @_name_boundary.callable_contract({'self': 'meadow_self_853d643', 'reader': 'meadow_reader_5c09d16'}, 'parse_v3')
    def meadow_parse_v3(meadow_self_853d643, meadow_reader_5c09d16: meadow_io.IOBase):
        """
        Parse trace version 3.
        :param reader: Stream to parse.
        :return: Generator for parsed kevents.
        """
        _name_boundary.attributes(meadow_self_853d643)['v3_header'] = meadow_Aligned(8, meadow_kd_header_v3).parse_stream(meadow_reader_5c09d16)
        meadow_reader_5c09d16.read(8 - meadow_RAW_VERSION_SIZE)
        meadow_seek_until(meadow_reader_5c09d16, meadow_TRACEV3_STACKSHOT_END)
        meadow_seek_until(meadow_reader_5c09d16, meadow_TRACEV3_THREADMAP_TAG)
        meadow_threadmap_0414e6f = meadow_kd_v3_threadmap.parse_stream(meadow_reader_5c09d16).threadmap
        _name_boundary.attributes(meadow_self_853d643)['set_thread_map'](meadow_threadmap_0414e6f)
        while True:
            meadow_seek_until(meadow_reader_5c09d16, meadow_TRACEV3_EVENTS_TAG)
            meadow_size_16b7ad1 = meadow_Int64ul.parse_stream(meadow_reader_5c09d16)
            meadow_reader_5c09d16.read(8)
            for meadow___7e567ba in range(meadow_size_16b7ad1 // meadow_KEVENT_SIZE):
                meadow_buf_0f71377 = meadow_reader_5c09d16.read(meadow_KEVENT_SIZE)
                yield meadow_from_kd_buf(meadow_buf_0f71377)
            if meadow_reader_5c09d16.read(len(meadow_TRACEV3_MORE_EVENTS)) != meadow_TRACEV3_MORE_EVENTS:
                break
        meadow_reader_5c09d16.seek(-8, 1)
        meadow_additional_data_b60b872 = meadow_kd_v3_additional_data.parse_stream(meadow_reader_5c09d16)
        _name_boundary.attributes(meadow_self_853d643)['trace_codes'] = ''
        _name_boundary.attributes(meadow_self_853d643)['kernel_extensions'] = {'Binaries': []}
        _name_boundary.attributes(meadow_self_853d643)['dyld_modules'] = {}
        _name_boundary.attributes(meadow_self_853d643)['images'] = {}
        _name_boundary.attributes(meadow_self_853d643)['processes'] = {}
        meadow_log_events_68341ff = []
        meadow_log_strings_135836d = {}
        for meadow_block_5fb12e3 in meadow_additional_data_b60b872:
            if meadow_block_5fb12e3.tag == meadow_TRACEV3_DYLD_MODULES:
                meadow_data_7cd05c5 = meadow_plistlib.loads(meadow_block_5fb12e3.data)
                if not _name_boundary.attributes(meadow_self_853d643)['dyld_modules']:
                    _name_boundary.attributes(meadow_self_853d643)['dyld_modules'].update(meadow_data_7cd05c5)
                else:
                    _name_boundary.attributes(meadow_self_853d643)['dyld_modules']['Binaries'].extend(meadow_data_7cd05c5['Binaries'])
            elif meadow_block_5fb12e3.tag == meadow_TRACEV3_TRACE_CODES:
                _name_boundary.attributes(meadow_self_853d643)['trace_codes'] += meadow_block_5fb12e3.data.decode()
            elif meadow_block_5fb12e3.tag == meadow_TRACEV3_PROCESSES:
                _name_boundary.attributes(meadow_self_853d643)['processes'] = meadow_plistlib.loads(meadow_block_5fb12e3.data)
            elif meadow_block_5fb12e3.tag == meadow_TRACEV3_KERNEL_EXTENSIONS:
                _name_boundary.attributes(meadow_self_853d643)['kernel_extensions']['Binaries'].extend(meadow_plistlib.loads(meadow_block_5fb12e3.data)['Binaries'])
            elif meadow_block_5fb12e3.tag == meadow_TRACEV3_IMAGES:
                _name_boundary.attributes(meadow_self_853d643)['images'] = meadow_plistlib.loads(meadow_block_5fb12e3.data)
            elif meadow_block_5fb12e3.tag == meadow_TRACEV3_LOG_EVENTS:
                meadow_log_events_68341ff.extend(meadow_plistlib.loads(meadow_block_5fb12e3.data)['Events'])
            elif meadow_block_5fb12e3.tag == meadow_TRACEV3_LOG_STRINGS:
                meadow_log_strings_135836d = {meadow_v_9c34be6: meadow_k_f15aad5 for meadow_k_f15aad5, meadow_v_9c34be6 in meadow_plistlib.loads(meadow_block_5fb12e3.data)['StringIndex'].items()}
        for meadow_event_55b3579 in meadow_log_events_68341ff:
            meadow_log_event_7600908 = _name_boundary.attributes(meadow_OsLogEvent)['from_raw_log_event'](meadow_event_55b3579, meadow_log_strings_135836d)
            if meadow_log_event_7600908.process and meadow_log_event_7600908.thread_identifier:
                _name_boundary.attributes(meadow_self_853d643)['threads_pids'][meadow_log_event_7600908.thread_identifier] = meadow_log_event_7600908.process_identifier
                _name_boundary.attributes(meadow_self_853d643)['pids_names'][meadow_log_event_7600908.process_identifier] = meadow_log_event_7600908.process
            yield meadow_log_event_7600908
_name_boundary.module_contract(globals(), {'RAW_VERSION2_BYTES': 'meadow_RAW_VERSION2_BYTES', 'kd_threadmap': 'meadow_kd_threadmap', 'TRACEV3_STACKSHOT_END': 'meadow_TRACEV3_STACKSHOT_END', 'KD_BUF_FORMAT': 'meadow_KD_BUF_FORMAT', 'kd_v3_additional_data': 'meadow_kd_v3_additional_data', 'TRACEV3_LOG_STRINGS': 'meadow_TRACEV3_LOG_STRINGS', 'Int64ul': 'meadow_Int64ul', 'kd_header_v3': 'meadow_kd_header_v3', 'seek_until': 'meadow_seek_until', 'TRACEV3_TRACE_CODES': 'meadow_TRACEV3_TRACE_CODES', 'plistlib': 'meadow_plistlib', 'Array': 'meadow_Array', 'BplistAdapter': 'meadow_BplistAdapter', 'namedtuple': 'meadow_namedtuple', 'Const': 'meadow_Const', 'Byte': 'meadow_Byte', 'Adapter': 'meadow_Adapter', 'RAW_VERSION_SIZE': 'meadow_RAW_VERSION_SIZE', 'TRACEV3_THREADMAP_TAG': 'meadow_TRACEV3_THREADMAP_TAG', 'GreedyRange': 'meadow_GreedyRange', 'from_kd_buf': 'meadow_from_kd_buf', 'struct': 'meadow_struct', 'TRACEV3_MORE_EVENTS': 'meadow_TRACEV3_MORE_EVENTS', 'Prefixed': 'meadow_Prefixed', 'io': 'meadow_io', 'kd_v3_threadmap': 'meadow_kd_v3_threadmap', 'TRACEV3_IMAGES': 'meadow_TRACEV3_IMAGES', 'TRACEV3_EVENTS_TAG': 'meadow_TRACEV3_EVENTS_TAG', 'Select': 'meadow_Select', 'KdBufParser': 'meadow_KdBufParser', 'TRACEV3_PROCESSES': 'meadow_TRACEV3_PROCESSES', 'Struct': 'meadow_Struct', 'Int32ul': 'meadow_Int32ul', 'TRACEV3_DYLD_MODULES': 'meadow_TRACEV3_DYLD_MODULES', 'TRACEV3_LOG_EVENTS': 'meadow_TRACEV3_LOG_EVENTS', 'GreedyBytes': 'meadow_GreedyBytes', 'kd_header_v2': 'meadow_kd_header_v2', 'KEVENT_SIZE': 'meadow_KEVENT_SIZE', 'Padding': 'meadow_Padding', 'OsLogEvent': 'meadow_OsLogEvent', 'TRACEV3_KERNEL_EXTENSIONS': 'meadow_TRACEV3_KERNEL_EXTENSIONS', 'Bytes': 'meadow_Bytes', 'ProcessData': 'meadow_ProcessData', 'CString': 'meadow_CString', 'FixedSized': 'meadow_FixedSized', 'Aligned': 'meadow_Aligned', 'RAW_VERSION3_BYTES': 'meadow_RAW_VERSION3_BYTES'})
