# Derived from tests/traces/test_turnstile.py; original copyright and license in ORIGIN.md and LICENSE.
import tracemeadow_boundary as _name_boundary
from tracemeadow.event_records import meadow_Kevent as meadow_Kevent

@_name_boundary.callable_contract({'traces_parser': 'meadow_traces_parser_c26fdcb'}, 'test_turnstile_waitq_add_thread_priority_queue')
def meadow_test_turnstile_waitq_add_thread_priority_queue(meadow_traces_parser_c26fdcb):
    meadow_events_18ba773 = [meadow_Kevent(timestamp=7476381345, data=b'\xa1!\xae\xdb\x9818\x81\x91\x1d\x00\x00\x00\x00\x00\x00%\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', values=(9311246762178912673, 7569, 37, 0), tid=7569, debugid=890241028, eventid=890241028, func_qualifier=0)]
    meadow_ret_dff3f33 = list(_name_boundary.attributes(meadow_traces_parser_c26fdcb)['feed_generator'](meadow_events_18ba773))[0]
    assert meadow_ret_dff3f33.turnstile == 9311246762178912673
    assert meadow_ret_dff3f33.tid == 7569
    assert meadow_ret_dff3f33.priority == 37

@_name_boundary.callable_contract({'traces_parser': 'meadow_traces_parser_78b4487'}, 'test_turnstile_update_thread_promotion_locked')
def meadow_test_turnstile_update_thread_promotion_locked(meadow_traces_parser_78b4487):
    meadow_events_41041d7 = [meadow_Kevent(timestamp=7497627001, data=b'a\xdc\xbf\xd9\x9818\x81\x1e\x1c\x00\x00\x00\x00\x00\x00/\x00\x00\x00\x00\x00\x00\x00%\x00\x00\x00\x00\x00\x00\x00', values=(9311246762146520161, 7198, 47, 37), tid=7593, debugid=890241036, eventid=890241036, func_qualifier=0)]
    meadow_ret_8141514 = list(_name_boundary.attributes(meadow_traces_parser_78b4487)['feed_generator'](meadow_events_41041d7))[0]
    assert meadow_ret_8141514.dst_turnstile == 9311246762146520161
    assert meadow_ret_8141514.tid == 7198
    assert meadow_ret_8141514.priority == 47
    assert meadow_ret_8141514.thread_link_priority == 37

@_name_boundary.callable_contract({'traces_parser': 'meadow_traces_parser_96a1183'}, 'test_turnstile_add_turnstile_promotion')
def meadow_test_turnstile_add_turnstile_promotion(meadow_traces_parser_96a1183):
    meadow_events_8c49621 = [meadow_Kevent(timestamp=7476382413, data=b'a\xb5o\xd8\x9818\x81!\xdd\xae\xdb\x9818\x81%\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', values=(9311246762124490081, 9311246762178960673, 37, 0), tid=6740, debugid=890241040, eventid=890241040, func_qualifier=0)]
    meadow_ret_ea69cff = list(_name_boundary.attributes(meadow_traces_parser_96a1183)['feed_generator'](meadow_events_8c49621))[0]
    assert meadow_ret_ea69cff.dst_turnstile == 9311246762124490081
    assert meadow_ret_ea69cff.src_turnstile == 9311246762178960673
    assert meadow_ret_ea69cff.src_ts_priority == 37

@_name_boundary.callable_contract({'traces_parser': 'meadow_traces_parser_efa836c'}, 'test_turnstile_remove_turnstile_promotion')
def meadow_test_turnstile_remove_turnstile_promotion(meadow_traces_parser_efa836c):
    meadow_events_e63b149 = [meadow_Kevent(timestamp=7476384288, data=b'\xa1\xc9\xc1\xd9\x9818\x81!\xdd\xae\xdb\x9818\x81\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', values=(9311246762146646433, 9311246762178960673, 0, 0), tid=6740, debugid=890241044, eventid=890241044, func_qualifier=0)]
    meadow_ret_b0ebf2b = list(_name_boundary.attributes(meadow_traces_parser_efa836c)['feed_generator'](meadow_events_e63b149))[0]
    assert meadow_ret_b0ebf2b.dst_turnstile == 9311246762146646433
    assert meadow_ret_b0ebf2b.src_turnstile == 9311246762178960673

@_name_boundary.callable_contract({'traces_parser': 'meadow_traces_parser_def98cb'}, 'test_turnstile_update_turnstile_promotion_locked')
def meadow_test_turnstile_update_turnstile_promotion_locked(meadow_traces_parser_def98cb):
    meadow_events_4b7696d = [meadow_Kevent(timestamp=7476376767, data=b'A\xaa\x9f\xd7\x9818\x81!\xd4A\xd9\x9818\x81\x00\x00\x00\x00\x00\x00\x00\x00%\x00\x00\x00\x00\x00\x00\x00', values=(9311246762110855745, 9311246762138260513, 0, 37), tid=7286, debugid=890241048, eventid=890241048, func_qualifier=0)]
    meadow_ret_2913d76 = list(_name_boundary.attributes(meadow_traces_parser_def98cb)['feed_generator'](meadow_events_4b7696d))[0]
    assert meadow_ret_2913d76.dst_turnstile == 9311246762110855745
    assert meadow_ret_2913d76.src_turnstile == 9311246762138260513
    assert meadow_ret_2913d76.src_ts_priority == 0
    assert meadow_ret_2913d76.src_turnstile_link_priority == 37

@_name_boundary.callable_contract({'traces_parser': 'meadow_traces_parser_8caa8cc'}, 'test_thread_update_turnstile_promotion_locked')
def meadow_test_thread_update_turnstile_promotion_locked(meadow_traces_parser_8caa8cc):
    meadow_events_f4eb966 = [meadow_Kevent(timestamp=7476383550, data=b'T\x1a\x00\x00\x00\x00\x00\x00a\xb5o\xd8\x9818\x81\x00\x00\x00\x00\x00\x00\x00\x00%\x00\x00\x00\x00\x00\x00\x00', values=(6740, 9311246762124490081, 0, 37), tid=6740, debugid=890241060, eventid=890241060, func_qualifier=0)]
    meadow_ret_088bc72 = list(_name_boundary.attributes(meadow_traces_parser_8caa8cc)['feed_generator'](meadow_events_f4eb966))[0]
    assert meadow_ret_088bc72.tid == 6740
    assert meadow_ret_088bc72.turnstile == 9311246762124490081
    assert meadow_ret_088bc72.turnstile_ts_priority == 0
    assert meadow_ret_088bc72.turnstile_link_priority == 37

@_name_boundary.callable_contract({'traces_parser': 'meadow_traces_parser_dd0b0a7'}, 'test_thread_not_waiting_on_turnstile')
def meadow_test_thread_not_waiting_on_turnstile(meadow_traces_parser_dd0b0a7):
    meadow_events_70836ae = [meadow_Kevent(timestamp=7476378853, data=b'v\x1c\x00\x00\x00\x00\x00\x00\n\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', values=(7286, 10, 0, 0), tid=7286, debugid=890241068, eventid=890241068, func_qualifier=0)]
    meadow_ret_bea9380 = list(_name_boundary.attributes(meadow_traces_parser_dd0b0a7)['feed_generator'](meadow_events_70836ae))[0]
    assert meadow_ret_bea9380.tid == 7286
    assert meadow_ret_bea9380.turnstile_max_hop == 10
    assert meadow_ret_bea9380.thread_hop == 0

@_name_boundary.callable_contract({'traces_parser': 'meadow_traces_parser_91622b5'}, 'test_turnstile_recompute_priority_locked')
def meadow_test_turnstile_recompute_priority_locked(meadow_traces_parser_91622b5):
    meadow_events_1bc49d4 = [meadow_Kevent(timestamp=7476425345, data=b'\x01\x93@\xd9\x9818\x81\x00\x00\x00\x00\x00\x00\x00\x00%\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', values=(9311246762138178305, 0, 37, 0), tid=7346, debugid=891289604, eventid=891289604, func_qualifier=0)]
    meadow_ret_d439fbe = list(_name_boundary.attributes(meadow_traces_parser_91622b5)['feed_generator'](meadow_events_1bc49d4))[0]
    assert meadow_ret_d439fbe.turnstile == 9311246762138178305
    assert meadow_ret_d439fbe.new_priority == 0
    assert meadow_ret_d439fbe.old_priority == 37

@_name_boundary.callable_contract({'traces_parser': 'meadow_traces_parser_ee1e17a'}, 'test_thread_recompute_user_promotion_locked')
def meadow_test_thread_recompute_user_promotion_locked(meadow_traces_parser_ee1e17a):
    meadow_events_0c77a3c = [meadow_Kevent(timestamp=7476383893, data=b'T\x1a\x00\x00\x00\x00\x00\x00%\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', values=(6740, 37, 0, 0), tid=6740, debugid=891289608, eventid=891289608, func_qualifier=0)]
    meadow_ret_bb694c1 = list(_name_boundary.attributes(meadow_traces_parser_ee1e17a)['feed_generator'](meadow_events_0c77a3c))[0]
    assert meadow_ret_bb694c1.tid == 6740
    assert meadow_ret_bb694c1.user_promotion_basepri == 37
    assert meadow_ret_bb694c1.thread_user_promotion_basepri == 0
_name_boundary.module_contract(globals(), {'test_turnstile_update_thread_promotion_locked': 'meadow_test_turnstile_update_thread_promotion_locked', 'test_turnstile_recompute_priority_locked': 'meadow_test_turnstile_recompute_priority_locked', 'test_thread_recompute_user_promotion_locked': 'meadow_test_thread_recompute_user_promotion_locked', 'test_thread_not_waiting_on_turnstile': 'meadow_test_thread_not_waiting_on_turnstile', 'test_turnstile_update_turnstile_promotion_locked': 'meadow_test_turnstile_update_turnstile_promotion_locked', 'Kevent': 'meadow_Kevent', 'test_turnstile_waitq_add_thread_priority_queue': 'meadow_test_turnstile_waitq_add_thread_priority_queue', 'test_thread_update_turnstile_promotion_locked': 'meadow_test_thread_update_turnstile_promotion_locked', 'test_turnstile_remove_turnstile_promotion': 'meadow_test_turnstile_remove_turnstile_promotion', 'test_turnstile_add_turnstile_promotion': 'meadow_test_turnstile_add_turnstile_promotion'})
