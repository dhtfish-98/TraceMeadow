# Derived from pykdebugparser/__main__.py; original attribution in ORIGIN.md and LICENSE.
import tracemeadow_boundary as _name_boundary
import json as meadow_json
import click as meadow_click
from tracemeadow.binary_stream import meadow_KdBufParser as meadow_KdBufParser
from tracemeadow.event_stream import meadow_PyKdebugParser as meadow_PyKdebugParser

import functools as meadow_functools
import itertools as meadow_itertools
import os as meadow_os
import stat as meadow_stat
import sys as meadow_sys
import datetime as meadow_datetime
import plistlib as meadow_plistlib
from tracemeadow.bounded_stream import TraceFormatError, MeadowLimits

meadow_OUTPUT_LIMIT = 16 * 1024 * 1024


class MeadowCLIError(meadow_click.ClickException):
    exit_code = 2


def meadow_command_errors(function):
    @meadow_functools.wraps(function)
    def invoke(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except (TraceFormatError, OSError) as error:
            raise MeadowCLIError(str(error)) from None
    return invoke


class MeadowLocalFile:
    def __init__(self, stream, identity):
        self.stream, self.identity = stream, identity
        self.received = 0
    def read(self, size):
        data = self.stream.read(size)
        self.received += len(data)
        if not data:
            current = meadow_os.fstat(self.stream.fileno())
            fields = ('st_dev', 'st_ino', 'st_size', 'st_mtime_ns', 'st_ctime_ns')
            if any(getattr(current, f) != getattr(self.identity, f) for f in fields) or self.received != self.identity.st_size:
                raise TraceFormatError('input changed or could not be completely read')
        return data
    def close(self):
        self.stream.close()


class MeadowDumpType(meadow_click.ParamType):
    name = 'local binary trace'
    def convert(self, value, param, ctx):
        if value == '-':
            return meadow_sys.stdin.buffer
        descriptor = None
        try:
            flags = meadow_os.O_RDONLY | meadow_os.O_NONBLOCK | getattr(meadow_os, 'O_CLOEXEC', 0) | meadow_os.O_NOFOLLOW
            descriptor = meadow_os.open(value, flags)
            identity = meadow_os.fstat(descriptor)
            if not meadow_stat.S_ISREG(identity.st_mode) or not 0 < identity.st_size <= MeadowLimits().input_bytes:
                raise OSError('input must be a nonempty regular file of at most 1 GiB')
            stream = MeadowLocalFile(meadow_os.fdopen(descriptor, 'rb'), identity)
            descriptor = None
            ctx.call_on_close(stream.close)
            return stream
        except OSError as error:
            self.fail(str(error), param, ctx)
        finally:
            if descriptor is not None:
                meadow_os.close(descriptor)


def meadow_make_parser(kind):
    context = meadow_click.get_current_context(silent=True)
    padding = (context.obj or {}).get('v2_padding', 0) if context is not None else 0
    return kind(v2_padding=padding)


class MeadowJSONEncoder(meadow_json.JSONEncoder):
    def default(self, value):
        if isinstance(value, bytes):
            if len(value) * 2 > meadow_OUTPUT_LIMIT:
                raise TraceFormatError('binary metadata exceeds JSON output limit')
            return {'$bytes_hex': value.hex()}
        if isinstance(value, meadow_datetime.datetime):
            return {'$datetime': value.isoformat()}
        if isinstance(value, meadow_plistlib.UID):
            return {'$plist_uid': value.data}
        raise TraceFormatError('metadata contains an unsupported JSON value')


def meadow_print_json(value):
    size = 0
    for text in MeadowJSONEncoder(indent=4).iterencode(value):
        size += len(text.encode('utf-8'))
        if size + 1 > meadow_OUTPUT_LIMIT:
            raise TraceFormatError('output byte limit exceeded; JSON report is incomplete')
        meadow_sys.stdout.write(text)
    meadow_sys.stdout.write('\n')


def meadow_drain(parser, reader):
    for _ in parser.meadow_parse(reader):
        pass


@meadow_click.group()
@meadow_click.option('--v2-padding', type=meadow_click.IntRange(0, 16 * 1024 * 1024), default=0, help='Explicit zero-filled v2 header padding in bytes; default 0 for packed streams.')
@_name_boundary.callable_contract({'v2_padding': 'meadow_v2_padding'}, 'cli')
def meadow_cli(meadow_v2_padding):
    meadow_click.get_current_context().obj = {'v2_padding': meadow_v2_padding}

@_name_boundary.callable_contract({'generator': 'meadow_generator_32e5514', 'count': 'meadow_count_427cd8f'}, 'print_with_count')
def meadow_print_with_count(meadow_generator_32e5514, meadow_count_427cd8f: int):
    if type(meadow_count_427cd8f) is not int or meadow_count_427cd8f < -1:
        raise TraceFormatError('count must be -1 or a nonnegative integer')
    iterator = iter(meadow_generator_32e5514)
    selected = iterator if meadow_count_427cd8f == -1 else meadow_itertools.islice(iterator, meadow_count_427cd8f)
    size = 0
    try:
        for record in selected:
            text = str(record)
            size += len(text.encode('utf-8')) + 1
            if size > meadow_OUTPUT_LIMIT:
                raise TraceFormatError('output byte limit exceeded; report is incomplete')
            print(text)
    finally:
        close = getattr(iterator, 'close', None)
        if close is not None:
            close()

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
meadow_dump_input = meadow_click.argument('kdebug_dump', type=MeadowDumpType())
meadow_count = meadow_click.option('-c', '--count', type=meadow_click.IntRange(min=-1), default=-1, help='Number of offline records to print. Omit to process to EOF; a count limit does not validate unread data.')
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
@meadow_command_errors
def meadow_kevents(meadow_kdebug_dump_e3f1b88, meadow_count_4f6f4b7, meadow_tid_7b5c468, meadow_show_tid_b1b6b4f, meadow_class_filters_b09143d, meadow_subclass_filters_533a508):
    meadow_parser_324e1b5 = meadow_make_parser(meadow_PyKdebugParser)
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
@meadow_command_errors
def meadow_traces(meadow_kdebug_dump_df4b896, meadow_count_b7e5182, meadow_tid_7913f10, meadow_process_4d5f1dc, meadow_show_tid_234f7ef, meadow_class_filters_43c4d4e, meadow_subclass_filters_20df600, meadow_color_a1bab7b):
    meadow_parser_50365ee = meadow_make_parser(meadow_PyKdebugParser)
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
@meadow_command_errors
def meadow_callstacks(meadow_kdebug_dump_2f1b4eb, meadow_count_dc3e171, meadow_tid_42241ff, meadow_process_20b232b, meadow_show_tid_da25732):
    meadow_parser_20ef99a = meadow_make_parser(meadow_PyKdebugParser)
    _name_boundary.attributes(meadow_parser_20ef99a)['filter_tid'] = meadow_tid_42241ff
    _name_boundary.attributes(meadow_parser_20ef99a)['filter_process'] = meadow_process_20b232b
    _name_boundary.attributes(meadow_parser_20ef99a)['show_tid'] = meadow_show_tid_da25732
    meadow_print_with_count(_name_boundary.attributes(meadow_parser_20ef99a)['formatted_callstacks'](meadow_kdebug_dump_2f1b4eb), meadow_count_dc3e171)

@meadow_cli.command(name='processes')
@meadow_dump_input
@_name_boundary.callable_contract({'kdebug_dump': 'meadow_kdebug_dump_7b64779'}, 'processes')
@meadow_command_errors
def meadow_processes(meadow_kdebug_dump_7b64779):
    meadow_parser_79a28a7 = meadow_make_parser(meadow_KdBufParser)
    meadow_drain(meadow_parser_79a28a7, meadow_kdebug_dump_7b64779)
    meadow_print_json(_name_boundary.attributes(meadow_parser_79a28a7)['processes'])

@meadow_cli.command(name='kexts')
@meadow_dump_input
@_name_boundary.callable_contract({'kdebug_dump': 'meadow_kdebug_dump_65c687f'}, 'kexts')
@meadow_command_errors
def meadow_kexts(meadow_kdebug_dump_65c687f):
    meadow_parser_9e82b04 = meadow_make_parser(meadow_KdBufParser)
    meadow_drain(meadow_parser_9e82b04, meadow_kdebug_dump_65c687f)
    meadow_print_json(_name_boundary.attributes(meadow_parser_9e82b04)['kernel_extensions'])

@meadow_cli.command(name='images')
@meadow_dump_input
@_name_boundary.callable_contract({'kdebug_dump': 'meadow_kdebug_dump_33d03b1'}, 'images')
@meadow_command_errors
def meadow_images(meadow_kdebug_dump_33d03b1):
    meadow_parser_d6f6357 = meadow_make_parser(meadow_KdBufParser)
    meadow_drain(meadow_parser_d6f6357, meadow_kdebug_dump_33d03b1)
    meadow_print_json(_name_boundary.attributes(meadow_parser_d6f6357)['images'])

@meadow_cli.command(name='logs')
@meadow_dump_input
@meadow_count
@meadow_tid_filter
@meadow_process_filter
@meadow_show_tid
@_name_boundary.callable_contract({'kdebug_dump': 'meadow_kdebug_dump_fa07b65', 'count': 'meadow_count_6c87172', 'tid': 'meadow_tid_8c08921', 'process': 'meadow_process_195e1e2', 'show_tid': 'meadow_show_tid_5dd5091'}, 'logs')
@meadow_command_errors
def meadow_logs(meadow_kdebug_dump_fa07b65, meadow_count_6c87172, meadow_tid_8c08921, meadow_process_195e1e2, meadow_show_tid_5dd5091):
    meadow_parser_9090e2f = meadow_make_parser(meadow_PyKdebugParser)
    _name_boundary.attributes(meadow_parser_9090e2f)['filter_tid'] = meadow_tid_8c08921
    _name_boundary.attributes(meadow_parser_9090e2f)['filter_process'] = meadow_process_195e1e2
    _name_boundary.attributes(meadow_parser_9090e2f)['show_tid'] = meadow_show_tid_5dd5091
    meadow_print_with_count(_name_boundary.attributes(meadow_parser_9090e2f)['formatted_logs'](meadow_kdebug_dump_fa07b65), meadow_count_6c87172)
if __name__ == '__main__':
    meadow_cli()
_name_boundary.module_contract(globals(), {'show_tid': 'meadow_show_tid', 'kevents': 'meadow_kevents', 'BASED_INT': 'meadow_BASED_INT', 'count': 'meadow_count', 'process_filter': 'meadow_process_filter', 'callstacks': 'meadow_callstacks', 'class_filter': 'meadow_class_filter', 'processes': 'meadow_processes', 'kexts': 'meadow_kexts', 'cli': 'meadow_cli', 'dump_input': 'meadow_dump_input', 'subclass_filter': 'meadow_subclass_filter', 'traces': 'meadow_traces', 'logs': 'meadow_logs', 'KdBufParser': 'meadow_KdBufParser', 'print_with_count': 'meadow_print_with_count', 'tid_filter': 'meadow_tid_filter', 'BasedIntParamType': 'meadow_BasedIntParamType', 'click': 'meadow_click', 'images': 'meadow_images', 'PyKdebugParser': 'meadow_PyKdebugParser', 'json': 'meadow_json'})
