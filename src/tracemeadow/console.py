# Derived from pykdebugparser/__main__.py; original copyright and license in ORIGIN.md and LICENSE.
import tracemeadow_boundary as _name_boundary
import json as meadow_json
import click as meadow_click
from tracemeadow.binary_stream import meadow_KdBufParser as meadow_KdBufParser
from tracemeadow.event_stream import meadow_PyKdebugParser as meadow_PyKdebugParser

@meadow_click.group()
@_name_boundary.callable_contract({}, 'cli')
def meadow_cli():
    pass

@_name_boundary.callable_contract({'generator': 'meadow_generator_32e5514', 'count': 'meadow_count_427cd8f'}, 'print_with_count')
def meadow_print_with_count(meadow_generator_32e5514, meadow_count_427cd8f: int):
    meadow_i_d1d031e = 0
    for meadow_obj_c61013c in meadow_generator_32e5514:
        if meadow_i_d1d031e == meadow_count_427cd8f:
            break
        print(meadow_obj_c61013c)
        meadow_i_d1d031e += 1

@_name_boundary.class_contract('BasedIntParamType', {'name': 'meadow_name'})
class meadow_BasedIntParamType(meadow_click.ParamType):
    meadow_name = 'based int'

    @_name_boundary.callable_contract({'self': 'meadow_self_5237a5e', 'value': 'meadow_value_cfbf4ea', 'param': 'meadow_param_b930cef', 'ctx': 'meadow_ctx_39cea4c'}, 'convert')
    def convert(meadow_self_5237a5e, meadow_value_cfbf4ea, meadow_param_b930cef, meadow_ctx_39cea4c):
        try:
            return int(meadow_value_cfbf4ea, 0)
        except ValueError:
            meadow_self_5237a5e.fail(f'{meadow_value_cfbf4ea!r} is not a valid int.', meadow_param_b930cef, meadow_ctx_39cea4c)
meadow_BASED_INT = meadow_BasedIntParamType()
meadow_dump_input = meadow_click.argument('kdebug_dump', type=meadow_click.File('rb'))
meadow_count = meadow_click.option('-c', '--count', type=meadow_click.INT, default=-1, help='Number of events to print. Omit to endless sniff.')
meadow_tid_filter = meadow_click.option('--tid', type=meadow_click.INT, default=None, help='Thread ID to filter. Omit for all.')
meadow_show_tid = meadow_click.option('--show-tid/--no-show-tid', default=False, help='Whether to print thread id or not.')
meadow_process_filter = meadow_click.option('--process', default=None, help='Process ID / name to filter. Omit for all.')
meadow_class_filter = meadow_click.option('-cf', '--class-filters', multiple=True, type=meadow_BASED_INT, help='Events class filter. Omit for all.')
meadow_subclass_filter = meadow_click.option('-sf', '--subclass-filters', multiple=True, type=meadow_BASED_INT, help='Events subclass filter. Omit for all.')

@meadow_cli.command(name='kevents')
@meadow_dump_input
@meadow_count
@meadow_tid_filter
@meadow_show_tid
@meadow_class_filter
@meadow_subclass_filter
@_name_boundary.callable_contract({'kdebug_dump': 'meadow_kdebug_dump_e3f1b88', 'count': 'meadow_count_4f6f4b7', 'tid': 'meadow_tid_7b5c468', 'show_tid': 'meadow_show_tid_b1b6b4f', 'class_filters': 'meadow_class_filters_b09143d', 'subclass_filters': 'meadow_subclass_filters_533a508'}, 'kevents')
def meadow_kevents(meadow_kdebug_dump_e3f1b88, meadow_count_4f6f4b7, meadow_tid_7b5c468, meadow_show_tid_b1b6b4f, meadow_class_filters_b09143d, meadow_subclass_filters_533a508):
    meadow_parser_324e1b5 = meadow_PyKdebugParser()
    _name_boundary.attributes(meadow_parser_324e1b5)['filter_class'] = meadow_class_filters_b09143d
    _name_boundary.attributes(meadow_parser_324e1b5)['filter_subclass'] = meadow_subclass_filters_533a508
    _name_boundary.attributes(meadow_parser_324e1b5)['filter_tid'] = meadow_tid_7b5c468
    _name_boundary.attributes(meadow_parser_324e1b5)['show_tid'] = meadow_show_tid_b1b6b4f
    meadow_print_with_count(_name_boundary.attributes(meadow_parser_324e1b5)['formatted_kevents'](meadow_kdebug_dump_e3f1b88), meadow_count_4f6f4b7)

@meadow_cli.command(name='traces')
@meadow_dump_input
@meadow_count
@meadow_tid_filter
@meadow_process_filter
@meadow_show_tid
@meadow_class_filter
@meadow_subclass_filter
@meadow_click.option('--color/--no-color', default=True, help='Whether to print with color or not.')
@_name_boundary.callable_contract({'kdebug_dump': 'meadow_kdebug_dump_df4b896', 'count': 'meadow_count_b7e5182', 'tid': 'meadow_tid_7913f10', 'process': 'meadow_process_4d5f1dc', 'show_tid': 'meadow_show_tid_234f7ef', 'class_filters': 'meadow_class_filters_43c4d4e', 'subclass_filters': 'meadow_subclass_filters_20df600', 'color': 'meadow_color_a1bab7b'}, 'traces')
def meadow_traces(meadow_kdebug_dump_df4b896, meadow_count_b7e5182, meadow_tid_7913f10, meadow_process_4d5f1dc, meadow_show_tid_234f7ef, meadow_class_filters_43c4d4e, meadow_subclass_filters_20df600, meadow_color_a1bab7b):
    meadow_parser_50365ee = meadow_PyKdebugParser()
    _name_boundary.attributes(meadow_parser_50365ee)['filter_tid'] = meadow_tid_7913f10
    _name_boundary.attributes(meadow_parser_50365ee)['filter_process'] = meadow_process_4d5f1dc
    _name_boundary.attributes(meadow_parser_50365ee)['filter_class'] = list(meadow_class_filters_43c4d4e)
    _name_boundary.attributes(meadow_parser_50365ee)['filter_subclass'] = list(meadow_subclass_filters_20df600)
    _name_boundary.attributes(meadow_parser_50365ee)['show_tid'] = meadow_show_tid_234f7ef
    _name_boundary.attributes(meadow_parser_50365ee)['color'] = meadow_color_a1bab7b
    meadow_print_with_count(_name_boundary.attributes(meadow_parser_50365ee)['formatted_traces'](meadow_kdebug_dump_df4b896), meadow_count_b7e5182)

@meadow_cli.command(name='callstacks')
@meadow_dump_input
@meadow_count
@meadow_tid_filter
@meadow_process_filter
@meadow_show_tid
@_name_boundary.callable_contract({'kdebug_dump': 'meadow_kdebug_dump_2f1b4eb', 'count': 'meadow_count_dc3e171', 'tid': 'meadow_tid_42241ff', 'process': 'meadow_process_20b232b', 'show_tid': 'meadow_show_tid_da25732'}, 'callstacks')
def meadow_callstacks(meadow_kdebug_dump_2f1b4eb, meadow_count_dc3e171, meadow_tid_42241ff, meadow_process_20b232b, meadow_show_tid_da25732):
    meadow_parser_20ef99a = meadow_PyKdebugParser()
    _name_boundary.attributes(meadow_parser_20ef99a)['filter_tid'] = meadow_tid_42241ff
    _name_boundary.attributes(meadow_parser_20ef99a)['filter_process'] = meadow_process_20b232b
    _name_boundary.attributes(meadow_parser_20ef99a)['show_tid'] = meadow_show_tid_da25732
    meadow_print_with_count(_name_boundary.attributes(meadow_parser_20ef99a)['formatted_callstacks'](meadow_kdebug_dump_2f1b4eb), meadow_count_dc3e171)

@meadow_cli.command(name='processes')
@meadow_dump_input
@_name_boundary.callable_contract({'kdebug_dump': 'meadow_kdebug_dump_7b64779'}, 'processes')
def meadow_processes(meadow_kdebug_dump_7b64779):
    meadow_parser_79a28a7 = meadow_KdBufParser({}, {})
    list(_name_boundary.attributes(meadow_parser_79a28a7)['parse'](meadow_kdebug_dump_7b64779))
    print(meadow_json.dumps(_name_boundary.attributes(meadow_parser_79a28a7)['processes'], indent=4))

@meadow_cli.command(name='kexts')
@meadow_dump_input
@_name_boundary.callable_contract({'kdebug_dump': 'meadow_kdebug_dump_65c687f'}, 'kexts')
def meadow_kexts(meadow_kdebug_dump_65c687f):
    meadow_parser_9e82b04 = meadow_KdBufParser({}, {})
    list(_name_boundary.attributes(meadow_parser_9e82b04)['parse'](meadow_kdebug_dump_65c687f))
    print(meadow_json.dumps(_name_boundary.attributes(meadow_parser_9e82b04)['kernel_extensions'], indent=4))

@meadow_cli.command(name='images')
@meadow_dump_input
@_name_boundary.callable_contract({'kdebug_dump': 'meadow_kdebug_dump_33d03b1'}, 'images')
def meadow_images(meadow_kdebug_dump_33d03b1):
    meadow_parser_d6f6357 = meadow_KdBufParser({}, {})
    list(_name_boundary.attributes(meadow_parser_d6f6357)['parse'](meadow_kdebug_dump_33d03b1))
    print(meadow_json.dumps(_name_boundary.attributes(meadow_parser_d6f6357)['images'], indent=4))

@meadow_cli.command(name='logs')
@meadow_dump_input
@meadow_count
@meadow_tid_filter
@meadow_process_filter
@meadow_show_tid
@_name_boundary.callable_contract({'kdebug_dump': 'meadow_kdebug_dump_fa07b65', 'count': 'meadow_count_6c87172', 'tid': 'meadow_tid_8c08921', 'process': 'meadow_process_195e1e2', 'show_tid': 'meadow_show_tid_5dd5091'}, 'logs')
def meadow_logs(meadow_kdebug_dump_fa07b65, meadow_count_6c87172, meadow_tid_8c08921, meadow_process_195e1e2, meadow_show_tid_5dd5091):
    meadow_parser_9090e2f = meadow_PyKdebugParser()
    _name_boundary.attributes(meadow_parser_9090e2f)['filter_tid'] = meadow_tid_8c08921
    _name_boundary.attributes(meadow_parser_9090e2f)['filter_process'] = meadow_process_195e1e2
    _name_boundary.attributes(meadow_parser_9090e2f)['show_tid'] = meadow_show_tid_5dd5091
    meadow_print_with_count(_name_boundary.attributes(meadow_parser_9090e2f)['formatted_logs'](meadow_kdebug_dump_fa07b65), meadow_count_6c87172)
if __name__ == '__main__':
    meadow_cli()
_name_boundary.module_contract(globals(), {'show_tid': 'meadow_show_tid', 'kevents': 'meadow_kevents', 'BASED_INT': 'meadow_BASED_INT', 'count': 'meadow_count', 'process_filter': 'meadow_process_filter', 'callstacks': 'meadow_callstacks', 'class_filter': 'meadow_class_filter', 'processes': 'meadow_processes', 'kexts': 'meadow_kexts', 'cli': 'meadow_cli', 'dump_input': 'meadow_dump_input', 'subclass_filter': 'meadow_subclass_filter', 'traces': 'meadow_traces', 'logs': 'meadow_logs', 'KdBufParser': 'meadow_KdBufParser', 'print_with_count': 'meadow_print_with_count', 'tid_filter': 'meadow_tid_filter', 'BasedIntParamType': 'meadow_BasedIntParamType', 'click': 'meadow_click', 'images': 'meadow_images', 'PyKdebugParser': 'meadow_PyKdebugParser', 'json': 'meadow_json'})
