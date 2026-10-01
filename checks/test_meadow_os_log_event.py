# Derived from tests/test_os_log_event.py; original copyright and license in ORIGIN.md and LICENSE.
import tracemeadow_boundary as _name_boundary
from datetime import datetime as meadow_datetime, timezone as meadow_timezone
from tracemeadow.log_records import meadow_OsLogEvent as meadow_OsLogEvent, meadow_OsLogType as meadow_OsLogType, meadow_FirehoseTracepointNamespace as meadow_FirehoseTracepointNamespace, meadow_FirehoseTracepointLogType as meadow_FirehoseTracepointLogType, meadow_FirehoseTracepointFlagsPcStyle as meadow_FirehoseTracepointFlagsPcStyle, meadow_FirehoseTracepointLogFlags as meadow_FirehoseTracepointLogFlags

@_name_boundary.callable_contract({}, 'test_parsing_raw_log_event')
def meadow_test_parsing_raw_log_event():
    meadow_raw_event_46d9038 = {'p': 1101, 'utz': {'mw': 480, 'dt': 1}, 'sub': 11, 'tid': 2263, 'ns': 59245485166, 'dm': {'s': 0, 'seg': [{'lp': 2013, 'p': {'rs': 2014, 'w': 0, 'p': 0, 't': [33]}, 'a': {'p': 1, 'c': 2, 'or': 164}}, {'lp': 2056, 'p': {'rs': 2057, 'w': 0, 'p': 72, 'ty': 2059, 'tn': 2018, 't': [33, 2058]}, 'a': {'p': 1, 'c': 3, 'or': b'\\x02\\x01\\x01\\x00I\\x01\\x00\\x00\\xea2\\x00\\x00\\x00\\x00\\x00\\x00\\xb8\\x08\\r\\x01\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x01\\x00\\x00\\x00\\x00\\x00\\x00\\x00P6\\x18\\x01\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x0086\\x18\\x01\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00'}}], 'pc': 2}, 'sip': 1100, 'mct': 1421891644, 's': 105, 'siu': b'\\xc4\\x9e\\x0c:\\xa9\\xc3:\\xb9\\x95\\xc4$b\\x80\\xf9#M', 'f': 2055, 't': 1024, 'pip': 1100, 'lt': 1, 'piu': b'\\xc4\\x9e\\x0c:\\xa9\\xc3:\\xb9\\x95\\xc4$b\\x80\\xf9#M', 'cm': 2053, 'ud': {'sec': 1633872873, 'usec': 810447}, 'send': 1101, 'cat': 2054, 'pid': 70, 'sio': 11269856, 'ti': 101451216374071556, 'b': b'l\\x87\\xdc\\xbf\\x06\\x01C[\\xbf\\x87\\xcc\\xf4\\xce\\x98\\x16 '}
    meadow_log_strings_0a69492 = {2053: '{"msg":"received AOP log", "log":{"flags":1,"seq":329,"data":[13034]}}', 1100: '/usr/libexec/locationd', 1101: 'locationd', 1024: '/usr/sbin/bluetoothd', 105: '%25s:%-5d %s: mActiveHighPriorityClientCount: %u, mActiveMediumPriorityClientCount: %u', 11: 'com.apple.locationd.Motion', 2054: 'AOP', 2055: '{"msg%{public}.0s":"received AOP log", "log":%{public, location:CMMotionCoprocessorReply_Log}.*P}', 2013: '{"msg', 2014: '%{public}.0s', 33: 'public', 164: '', 2056: '":"received AOP log", "log":', 2057: '%{public, location:CMMotionCoprocessorReply_Log}.*P', 2058: 'location:CMMotionCoprocessorReply_Log', 2018: 'location', 2059: 'CMMotionCoprocessorReply_Log'}
    meadow_parsed_event_b975418 = _name_boundary.attributes(meadow_OsLogEvent)['from_raw_log_event'](meadow_raw_event_46d9038, meadow_log_strings_0a69492)
    assert meadow_parsed_event_b975418.process == 'locationd'
    assert meadow_parsed_event_b975418.unix_timezone == {'minutes_west': 480, 'dst_time': 1}
    assert meadow_parsed_event_b975418.subsystem == 'com.apple.locationd.Motion'
    assert meadow_parsed_event_b975418.thread_identifier == 2263
    assert meadow_parsed_event_b975418.continuous_nanoseconds_since_boot == 59245485166
    assert meadow_parsed_event_b975418.sender_image_path == '/usr/libexec/locationd'
    assert meadow_parsed_event_b975418.mach_continuous_timestamp == 1421891644
    assert meadow_parsed_event_b975418.size == 105
    assert meadow_parsed_event_b975418.sender_image_uuid == b'\\xc4\\x9e\\x0c:\\xa9\\xc3:\\xb9\\x95\\xc4$b\\x80\\xf9#M'
    assert meadow_parsed_event_b975418.format_string == '{"msg%{public}.0s":"received AOP log", "log":%{public, location:CMMotionCoprocessorReply_Log}.*P}'
    assert meadow_parsed_event_b975418.type_ == 1024
    assert meadow_parsed_event_b975418.process_image_path == '/usr/libexec/locationd'
    assert meadow_parsed_event_b975418.log_type == meadow_OsLogType.INFO
    assert meadow_parsed_event_b975418.process_image_uuid == b'\\xc4\\x9e\\x0c:\\xa9\\xc3:\\xb9\\x95\\xc4$b\\x80\\xf9#M'
    assert meadow_parsed_event_b975418.composed_message == '{"msg":"received AOP log", "log":{"flags":1,"seq":329,"data":[13034]}}'
    assert meadow_parsed_event_b975418.unix_date == meadow_datetime(2021, 10, 10, 13, 34, 33, 810447, tzinfo=meadow_timezone.utc)
    assert meadow_parsed_event_b975418.sender == 'locationd'
    assert meadow_parsed_event_b975418.category == 'AOP'
    assert meadow_parsed_event_b975418.process_identifier == 70
    assert meadow_parsed_event_b975418.sender_image_offset == 11269856
    assert meadow_parsed_event_b975418.trace_identifier.namespace == meadow_FirehoseTracepointNamespace.log
    assert meadow_parsed_event_b975418.trace_identifier.type_ == meadow_FirehoseTracepointLogType.info
    assert not meadow_parsed_event_b975418.trace_identifier.has_large_offset
    assert not meadow_parsed_event_b975418.trace_identifier.has_unique_pid
    assert meadow_parsed_event_b975418.trace_identifier.pc_style == meadow_FirehoseTracepointFlagsPcStyle.main_exe
    assert not meadow_parsed_event_b975418.trace_identifier.has_current_aid
    assert meadow_parsed_event_b975418.trace_identifier.flags == meadow_FirehoseTracepointLogFlags.has_subsystem
    assert meadow_parsed_event_b975418.boot_uuid == b'l\\x87\\xdc\\xbf\\x06\\x01C[\\xbf\\x87\\xcc\\xf4\\xce\\x98\\x16 '

@_name_boundary.callable_contract({}, 'test_parsing_event_with_backtrace')
def meadow_test_parsing_event_with_backtrace():
    meadow_raw_event_d7ae89f = {'p': 191, 'utz': {'mw': 480, 'dt': 1}, 'sub': 192, 'tid': 1117540, 'ns': 589505000739000, 'bt': [{'iu': b'\x94\x82\x8e\xdd`p1<\x93\x1d\xab\xa0\x18\xf0f\\', 'io': 1264156}, {'iu': b'\x94\x82\x8e\xdd`p1<\x93\x1d\xab\xa0\x18\xf0f\\', 'io': 46724}, {'iu': b'\x94\x82\x8e\xdd`p1<\x93\x1d\xab\xa0\x18\xf0f\\', 'io': 29436}, {'iu': b'\x94\x82\x8e\xdd`p1<\x93\x1d\xab\xa0\x18\xf0f\\', 'io': 29160}, {'iu': b'\x94\x82\x8e\xdd`p1<\x93\x1d\xab\xa0\x18\xf0f\\', 'io': 1082752}, {'iu': b'\x94\x82\x8e\xdd`p1<\x93\x1d\xab\xa0\x18\xf0f\\', 'io': 1082296}, {'iu': b'\x94\x82\x8e\xdd`p1<\x93\x1d\xab\xa0\x18\xf0f\\', 'io': 1081596}, {'iu': b'\xe8\xa6\x00Q\x0ch5\xae\xae\xfd\x9d\x97\xcc\x7f&\x96', 'io': 66784}, {'iu': b'\xe8\xa6\x00Q\x0ch5\xae\xae\xfd\x9d\x97\xcc\x7f&\x96', 'io': 67844}, {'iu': b'\x95\x9c\xd6\xe4\x0c\xe70"\xb7<\x8b6\xf7\x9fGE', 'io': 14864}, {'iu': b'\x95\x9c\xd6\xe4\x0c\xe70"\xb7<\x8b6\xf7\x9fGE', 'io': 129188}, {'iu': b'\x95\x9c\xd6\xe4\x0c\xe70"\xb7<\x8b6\xf7\x9fGE', 'io': 44932}, {'iu': b'\x95\x9c\xd6\xe4\x0c\xe70"\xb7<\x8b6\xf7\x9fGE', 'io': 132596}, {'iu': b'\x95\x9c\xd6\xe4\x0c\xe70"\xb7<\x8b6\xf7\x9fGE', 'io': 44932}, {'iu': b'\x95\x9c\xd6\xe4\x0c\xe70"\xb7<\x8b6\xf7\x9fGE', 'io': 48144}, {'iu': b'\x95\x9c\xd6\xe4\x0c\xe70"\xb7<\x8b6\xf7\x9fGE', 'io': 90904}, {'iu': b'\xbc\x1c\xe0\xc6\xa9\xf29k\x9a\xfbb=:\xcdX\x81', 'io': 4528}, {'iu': b'\xbc\x1c\xe0\xc6\xa9\xf29k\x9a\xfbb=:\xcdX\x81', 'io': 3920}], 'sip': 190, 'mct': 14148120017736, 'dm': {'s': 0, 'seg': [{'p': {'rs': 100, 'w': 0, 'p': 0}, 'a': {'p': 1, 'c': 2, 'or': 11448}}, {'lp': 11449, 'p': {'rs': 196, 'w': 0, 'p': 0, 't': [17]}, 'a': {'p': 1, 'c': 2, 'or': 498}}], 'pc': 2}, 's': 270, 'siu': b'\x94\x82\x8e\xdd`p1<\x93\x1d\xab\xa0\x18\xf0f\\', 'f': 11447, 't': 1024, 'ttl': 14, 'aid': 442, 'pip': 190, 'lt': 17, 'piu': b'\x94\x82\x8e\xdd`p1<\x93\x1d\xab\xa0\x18\xf0f\\', 'cm': 11446, 'ud': {'sec': 1634714583, 'usec': 341124}, 'send': 191, 'cat': 126, 'pid': 118, 'sio': 1264156, 'ti': 7433102699991300, 'b': b'\x08\xcc\xed\xc6g\xb8O\xe9\xa4\xf0\xa8d\xa0\xba^\x1e'}
    meadow_log_strings_6c5cf0b = {191: 'corespeechd', 11446: '-[CSFallbackAudioSessionReleaseProvider fallbackDeactivateAudioSession:error:] Cannot deactivateAudioSession with (null)', 190: '/System/Library/PrivateFrameworks/CoreSpeech.framework/corespeechd', 192: 'com.apple.corespeech', 126: 'Framework', 11447: '%s Cannot deactivateAudioSession with %{public}@', 100: '%s', 11448: '-[CSFallbackAudioSessionReleaseProvider fallbackDeactivateAudioSession:error:]', 11449: ' Cannot deactivateAudioSession with', 196: '%{public}@', 17: 'public', 498: ''}
    meadow_parsed_event_d6bfe26 = _name_boundary.attributes(meadow_OsLogEvent)['from_raw_log_event'](meadow_raw_event_d7ae89f, meadow_log_strings_6c5cf0b)
    assert meadow_parsed_event_d6bfe26.process == 'corespeechd'
    assert meadow_parsed_event_d6bfe26.unix_timezone == {'dst_time': 1, 'minutes_west': 480}
    assert meadow_parsed_event_d6bfe26.subsystem == 'com.apple.corespeech'
    assert meadow_parsed_event_d6bfe26.thread_identifier == 1117540
    assert meadow_parsed_event_d6bfe26.continuous_nanoseconds_since_boot == 589505000739000
    assert meadow_parsed_event_d6bfe26.backtrace == [{'image_uuid': b'\x94\x82\x8e\xdd`p1<\x93\x1d\xab\xa0\x18\xf0f\\', 'image_offset': 1264156}, {'image_uuid': b'\x94\x82\x8e\xdd`p1<\x93\x1d\xab\xa0\x18\xf0f\\', 'image_offset': 46724}, {'image_uuid': b'\x94\x82\x8e\xdd`p1<\x93\x1d\xab\xa0\x18\xf0f\\', 'image_offset': 29436}, {'image_uuid': b'\x94\x82\x8e\xdd`p1<\x93\x1d\xab\xa0\x18\xf0f\\', 'image_offset': 29160}, {'image_uuid': b'\x94\x82\x8e\xdd`p1<\x93\x1d\xab\xa0\x18\xf0f\\', 'image_offset': 1082752}, {'image_uuid': b'\x94\x82\x8e\xdd`p1<\x93\x1d\xab\xa0\x18\xf0f\\', 'image_offset': 1082296}, {'image_uuid': b'\x94\x82\x8e\xdd`p1<\x93\x1d\xab\xa0\x18\xf0f\\', 'image_offset': 1081596}, {'image_uuid': b'\xe8\xa6\x00Q\x0ch5\xae\xae\xfd\x9d\x97\xcc\x7f&\x96', 'image_offset': 66784}, {'image_uuid': b'\xe8\xa6\x00Q\x0ch5\xae\xae\xfd\x9d\x97\xcc\x7f&\x96', 'image_offset': 67844}, {'image_uuid': b'\x95\x9c\xd6\xe4\x0c\xe70"\xb7<\x8b6\xf7\x9fGE', 'image_offset': 14864}, {'image_uuid': b'\x95\x9c\xd6\xe4\x0c\xe70"\xb7<\x8b6\xf7\x9fGE', 'image_offset': 129188}, {'image_uuid': b'\x95\x9c\xd6\xe4\x0c\xe70"\xb7<\x8b6\xf7\x9fGE', 'image_offset': 44932}, {'image_uuid': b'\x95\x9c\xd6\xe4\x0c\xe70"\xb7<\x8b6\xf7\x9fGE', 'image_offset': 132596}, {'image_uuid': b'\x95\x9c\xd6\xe4\x0c\xe70"\xb7<\x8b6\xf7\x9fGE', 'image_offset': 44932}, {'image_uuid': b'\x95\x9c\xd6\xe4\x0c\xe70"\xb7<\x8b6\xf7\x9fGE', 'image_offset': 48144}, {'image_uuid': b'\x95\x9c\xd6\xe4\x0c\xe70"\xb7<\x8b6\xf7\x9fGE', 'image_offset': 90904}, {'image_uuid': b'\xbc\x1c\xe0\xc6\xa9\xf29k\x9a\xfbb=:\xcdX\x81', 'image_offset': 4528}, {'image_uuid': b'\xbc\x1c\xe0\xc6\xa9\xf29k\x9a\xfbb=:\xcdX\x81', 'image_offset': 3920}]
    assert meadow_parsed_event_d6bfe26.sender_image_path == '/System/Library/PrivateFrameworks/CoreSpeech.framework/corespeechd'
    assert meadow_parsed_event_d6bfe26.mach_continuous_timestamp == 14148120017736
    assert meadow_parsed_event_d6bfe26.size == 270
    assert meadow_parsed_event_d6bfe26.sender_image_uuid == b'\x94\x82\x8e\xdd`p1<\x93\x1d\xab\xa0\x18\xf0f\\'
    assert meadow_parsed_event_d6bfe26.format_string == '%s Cannot deactivateAudioSession with %{public}@'
    assert meadow_parsed_event_d6bfe26.type_ == 1024
    assert meadow_parsed_event_d6bfe26.time_to_live == 14
    assert meadow_parsed_event_d6bfe26.activity_identifier == 442
    assert meadow_parsed_event_d6bfe26.process_image_path == '/System/Library/PrivateFrameworks/CoreSpeech.framework/corespeechd'
    assert meadow_parsed_event_d6bfe26.log_type == meadow_OsLogType.FAULT
    assert meadow_parsed_event_d6bfe26.process_image_uuid == b'\x94\x82\x8e\xdd`p1<\x93\x1d\xab\xa0\x18\xf0f\\'
    assert meadow_parsed_event_d6bfe26.composed_message == '-[CSFallbackAudioSessionReleaseProvider fallbackDeactivateAudioSession:error:] Cannot deactivateAudioSession with (null)'
    assert meadow_parsed_event_d6bfe26.unix_date == meadow_datetime(2021, 10, 20, 7, 23, 3, 341124, tzinfo=meadow_timezone.utc)
    assert meadow_parsed_event_d6bfe26.sender == 'corespeechd'
    assert meadow_parsed_event_d6bfe26.category == 'Framework'
    assert meadow_parsed_event_d6bfe26.process_identifier == 118
    assert meadow_parsed_event_d6bfe26.sender_image_offset == 1264156
    assert meadow_parsed_event_d6bfe26.trace_identifier.namespace == meadow_FirehoseTracepointNamespace.log
    assert meadow_parsed_event_d6bfe26.trace_identifier.type_ == meadow_FirehoseTracepointLogType.fault
    assert not meadow_parsed_event_d6bfe26.trace_identifier.has_large_offset
    assert not meadow_parsed_event_d6bfe26.trace_identifier.has_unique_pid
    assert meadow_parsed_event_d6bfe26.trace_identifier.has_current_aid
    assert meadow_parsed_event_d6bfe26.trace_identifier.pc_style == meadow_FirehoseTracepointFlagsPcStyle.main_exe
    assert meadow_parsed_event_d6bfe26.trace_identifier.flags == meadow_FirehoseTracepointLogFlags.has_context_data | meadow_FirehoseTracepointLogFlags.has_rules | meadow_FirehoseTracepointLogFlags.has_subsystem
    assert meadow_parsed_event_d6bfe26.trace_identifier.code == 1730654
    assert meadow_parsed_event_d6bfe26.boot_uuid == b'\x08\xcc\xed\xc6g\xb8O\xe9\xa4\xf0\xa8d\xa0\xba^\x1e'
_name_boundary.module_contract(globals(), {'timezone': 'meadow_timezone', 'FirehoseTracepointNamespace': 'meadow_FirehoseTracepointNamespace', 'OsLogEvent': 'meadow_OsLogEvent', 'FirehoseTracepointLogFlags': 'meadow_FirehoseTracepointLogFlags', 'test_parsing_event_with_backtrace': 'meadow_test_parsing_event_with_backtrace', 'FirehoseTracepointFlagsPcStyle': 'meadow_FirehoseTracepointFlagsPcStyle', 'OsLogType': 'meadow_OsLogType', 'FirehoseTracepointLogType': 'meadow_FirehoseTracepointLogType', 'test_parsing_raw_log_event': 'meadow_test_parsing_raw_log_event', 'datetime': 'meadow_datetime'})
