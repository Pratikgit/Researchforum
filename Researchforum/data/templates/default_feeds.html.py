# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1493536167.914662
_enable_loop = True
_template_filename = '/home/mayur/Researchforum/Researchforum/researchforum/templates/default_feeds.html'
_template_uri = '/default_feeds.html'
_source_encoding = 'utf-8'
from markupsafe import escape
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'<!DOCTYPE html>\n<html >\n<head>\n  <meta charset="UTF-8">\n  <title>Login Form with Materializecss</title>\n  \n</head>\n\n<body>\n  <html>\n\n<head>\n  <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">\n  <link href="/css/materialize.css" type="text/css" rel="stylesheet" media="screen,projection"/> \n  <link href="/css/random.css" type="text/css" rel="stylesheet" media="screen,projection"/>\n  <link href="/css/style.css" type="text/css" rel="stylesheet" media="screen,projection"/>\n  \n  <style>\n    body {\n      display: flex;\n      min-height: 100vh;\n      flex-direction: column;\n    }\n\n    main {\n      flex: 1 0 auto;\n    }\n\n    body {\n      background-image: url("/images/background.png");\n    }\n\n    .input-field input[type=date]:focus + label,\n    .input-field input[type=text]:focus + label,\n    .input-field input[type=email]:focus + label,\n    .input-field input[type=password]:focus + label {\n      color: #e91e63;\n    }\n\n    .input-field input[type=date]:focus,\n    .input-field input[type=text]:focus,\n    .input-field input[type=email]:focus,\n    .input-field input[type=password]:focus {\n      border-bottom: 2px solid #e91e63;\n      box-shadow: none;\n    }\n  </style>\n</head>\n\n<body>\n')
        __M_writer(escape(c.final_papers))
        __M_writer(u'\n  <script src="/js/jquery-2.1.1.min.js"></script>\n  <script src="/js/materialize.js"></script>\n</body>\n\n</html>\n  \n  \n</body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"24": 51, "17": 0, "31": 25, "25": 51, "23": 1}, "uri": "/default_feeds.html", "filename": "/home/mayur/Researchforum/Researchforum/researchforum/templates/default_feeds.html"}
__M_END_METADATA
"""
