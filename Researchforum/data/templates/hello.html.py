# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1493494444.605563
_enable_loop = True
_template_filename = '/home/mayur/Researchforum/Researchforum/researchforum/templates/hello.html'
_template_uri = '/hello.html'
_source_encoding = 'utf-8'
from markupsafe import escape
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'<html>\n    Welcom ')
        __M_writer(escape(c.name))
        __M_writer(u' to Hackathon Project...\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"24": 2, "17": 0, "31": 25, "25": 2, "23": 1}, "uri": "/hello.html", "filename": "/home/mayur/Researchforum/Researchforum/researchforum/templates/hello.html"}
__M_END_METADATA
"""
