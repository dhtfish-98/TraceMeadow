"""Owned event sequences validate aggregation and nearest-image attribution boundaries."""
from types import SimpleNamespace
from uuid import UUID
import pytest
from tracemeadow.event_records import meadow_Kevent
from tracemeadow.trace_stream import meadow_TracesParser
from tracemeadow.stack_stream import meadow_CallstacksParser, meadow_Frame, meadow_Callstack
from tracemeadow.event_stream import meadow_PyKdebugParser
from tracemeadow.handlers.performance_events import meadow_PerfEvent
from tracemeadow.handlers.image_events import meadow_DyldUuidMapA, meadow_DyldLaunchExecutable
from tracemeadow.bounded_stream import TraceFormatError


def event(timestamp, eventid=4, qualifier=0, tid=7, data=bytes(32), values=(0,0,0,0)):
    return meadow_Kevent(timestamp,data,values,tid,eventid|qualifier,eventid,qualifier)


def parser(**limits):
    result=meadow_TracesParser({4:'OWNED_A',8:'OWNED_B'}, {}, {}, **limits)
    result.handlers.update(OWNED_A=lambda _,events:[e.timestamp for e in events],
                           OWNED_B=lambda _,events:[e.timestamp for e in events])
    return result


def test_nested_groups_replacement_cleanup_and_order():
    p=parser()
    assert p.feed(event(1,4,1)) is None
    assert p.feed(event(2,8,1)) is None
    assert p.feed(event(3))==[3]
    assert p.feed(event(4,8,2))==[2,3,4]
    assert p.feed(event(5,4,2))==[1,2,3,4,5]
    assert p.on_going_events=={} and p._groups==p._references==0
    p.feed(event(6,4,1));p.feed(event(7,4,1))
    assert p.feed(event(8,4,2))==[7,8]  # same-ID start replaces the previous group
    assert p.feed(event(9,4,2)) is None  # unmatched end remains an ignored record


@pytest.mark.parametrize('limits,sequence',[
    ({'max_groups':1},[event(1,4,1),event(2,8,1)]),
    ({'max_references':1},[event(1,4,1),event(2)]),
    ({'max_group_events':1},[event(1,4,1),event(2)]),
])
def test_pending_limits_fail_before_group_mutation(limits,sequence):
    p=parser(**limits);p.feed(sequence[0])
    before={tid:{eid:list(items) for eid,items in groups.items()} for tid,groups in p.on_going_events.items()}
    with pytest.raises(TraceFormatError,match='limit'):p.feed(sequence[1])
    assert p.on_going_events==before and p._groups==p._references==1


def test_generator_budget_and_unsupported_qualifier():
    p=parser(max_events=2)
    generator=p.feed_generator([event(1),event(2),event(3)])
    assert next(generator)==[1] and next(generator)==[2]
    with pytest.raises(TraceFormatError,match='event limit'):next(generator)
    with pytest.raises(TraceFormatError,match='qualifier'):parser().feed(event(1,qualifier=9))


def test_empty_unknown_and_bad_handler_sequences():
    p=parser(max_group_events=2)
    assert p.parse_event_list([]) is None and p.parse_event_list([event(1,100)]) is None
    with pytest.raises(TraceFormatError):p.parse_event_list(iter([event(1),event(2),event(3)]))
    p.handlers['OWNED_A']=lambda _,records:records[5]
    with pytest.raises(TraceFormatError,match='handler event data'):p.feed(event(1))


def test_global_group_budget_covers_both_state_tables():
    p=parser(max_groups=1)
    p.trace_codes[12]='TRACE_DATA_EXEC'
    p.feed(event(1,12,1))
    with pytest.raises(TraceFormatError,match='group limit'):p.feed(event(2,4,1))
    assert p._groups==1 and p.on_going_events=={}


def test_vnode_path_assembly_and_actual_limits():
    first=event(1,qualifier=1,data=bytes(8)+b'/owned'+bytes(18),values=(42,0,0,0))
    last=event(2,qualifier=2,data=b'/tail'+bytes(27))
    node=list(meadow_TracesParser.vnode_generator([first,last]))[0]
    assert node.vnode_id==42 and node.path=='/owned/tail' and node.ktraces==[first,last]
    with pytest.raises(TraceFormatError,match='path byte limit'):
        list(meadow_TracesParser.vnode_generator([first,last],max_path_bytes=40))
    with pytest.raises(TraceFormatError,match='event limit'):
        list(meadow_TracesParser.vnode_generator([first,last],max_events=1))
    with pytest.raises(TraceFormatError,match='encoding'):
        list(meadow_TracesParser.vnode_generator([event(1,qualifier=3,data=bytes(8)+bytes([255]))]))


def test_callstack_image_boundaries_duplicate_address_and_aliases():
    first,second=UUID(int=1),UUID(int=2)
    addresses,identifiers=[],[]
    p=meadow_CallstacksParser(dyld_addresses=addresses,dyld_uuids=identifiers)
    p.insert_image(address=0x2000,uuid=second);p.insert_image(address=0x1000,uuid=first)
    p.insert_image(address=0x1000,uuid=second)
    sample=meadow_PerfEvent([event(55,tid=77)],[],0,cs_frames=[0xfff,0x1000,0x1fff,0x2000])
    result=list(p.feed_generator(generator=[sample]))[0]
    assert result.timestamp==55 and result.tid==77
    assert result.frames==[meadow_Frame(0xfff,None,None),meadow_Frame(0x1000,first,0),
                           meadow_Frame(0x1fff,first,0xfff),meadow_Frame(0x2000,second,0)]
    assert addresses==[0x1000,0x2000] and identifiers==[first,second]


@pytest.mark.parametrize('address',[-1,2**64,True,1.5,'1'])
def test_invalid_addresses_do_not_modify_owned_tables(address):
    p=meadow_CallstacksParser([],[])
    with pytest.raises(TraceFormatError):p.insert_image(address,None)
    assert p.dyld_addresses==p.dyld_uuids==[]


@pytest.mark.parametrize('addresses,identifiers',[
    ([2,1],[None,None]),([1],[]),([True],[None]),([-1],[None])
])
def test_inconsistent_initial_tables(addresses,identifiers):
    with pytest.raises(TraceFormatError):meadow_CallstacksParser(addresses,identifiers)


def test_frame_trace_and_launch_limits_and_no_partial_sample():
    p=meadow_CallstacksParser([],[],max_frames=1,max_traces=1,max_images=1)
    sample=meadow_PerfEvent([event(1)],[],0,cs_frames=iter([1,2]))
    generator=p.feed_generator([sample])
    with pytest.raises(TraceFormatError,match='frame limit'):next(generator)
    p.insert_image(1,None)
    with pytest.raises(TraceFormatError,match='image limit'):p.insert_image(2,None)
    assert p.dyld_addresses==[1] and p.dyld_uuids==[None]
    with pytest.raises(TraceFormatError,match='trace limit'):
        list(p.feed_generator([SimpleNamespace(),SimpleNamespace()]))
    images=[meadow_DyldUuidMapA([],None,1,0),meadow_DyldUuidMapA([],None,1,0)]
    launch=meadow_DyldLaunchExecutable([],1,iter(images))
    with pytest.raises(TraceFormatError,match='launch image list'):
        list(p.feed_generator([launch]))
    sample=meadow_PerfEvent([],[],0,cs_frames=[])
    with pytest.raises(TraceFormatError,match='source event'):list(p.feed_generator([sample]))


@pytest.mark.parametrize('limit',[0,-1,True,1.5])
def test_invalid_parser_limits(limit):
    with pytest.raises(ValueError):meadow_CallstacksParser([],[],max_frames=limit)
    with pytest.raises(ValueError):parser(max_groups=limit)


def test_indentation_is_bounded_before_whole_stack_materialization():
    p=meadow_PyKdebugParser();p.show_process=False
    sample=meadow_Callstack(1,7,[meadow_Frame(1,None,None)]*10000)
    with pytest.raises(TraceFormatError,match='formatting byte limit'):p._format_callstack(sample)
    assert p._format_callstack(meadow_Callstack(1,7,[meadow_Frame(1,None,None),meadow_Frame(2,None,None)]))=='1 \n0x0000000000000001\n 0x0000000000000002'
