# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1493515067.74376
_enable_loop = True
_template_filename = '/home/mayur/Researchforum/Researchforum/researchforum/templates/signup.html'
_template_uri = '/signup.html'
_source_encoding = 'utf-8'
from markupsafe import escape
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer(u'<!DOCTYPE html>\n<html >\n<head>\n  <meta charset="UTF-8">\n  <title>Login Form with Materializecss</title>\n  \n</head>\n\n<body>\n  <html>\n\n<head>\n  <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">\n  <link href="/css/materialize.css" type="text/css" rel="stylesheet" media="screen,projection"/>\n  <link href="/css/style.css" type="text/css" rel="stylesheet" media="screen,projection"/>\n  \n  <style>\n    body {\n      display: flex;\n      min-height: 100vh;\n      flex-direction: column;\n    }\n\n    main {\n      flex: 1 0 auto;\n    }\n\n    body {\n      background-image: url("/images/background.png");\n    }\n\n    .input-field input[type=date]:focus + label,\n    .input-field input[type=text]:focus + label,\n    .input-field input[type=email]:focus + label,\n    .input-field input[type=password]:focus + label {\n      color: #e91e63;\n    }\n\n    .input-field input[type=date]:focus,\n    .input-field input[type=text]:focus,\n    .input-field input[type=email]:focus,\n    .input-field input[type=password]:focus {\n      border-bottom: 2px solid #e91e63;\n      box-shadow: none;\n    }\n  </style>\n</head>\n\n<body>\n  <div class="section"></div>\n  <main>\n    <center>\n    <h4 class="white-text">Research Forum</h4>\n      <p class="white-text">Explore the world of Research !</p>\n      <!-- class="indigo-text" -->\n\n      <div class="container">\n        <div class="z-depth-1 grey lighten-4 row" style="display: inline-block; padding: 10px 48px 0px 48px; border: 1px solid #EEE;width: 50%">\n\n          <form class="col s12" method="post" action="http://127.0.0.1:5000/action/create_user">\n            <div class=\'row\'>\n              <div class=\'col s12\'>\n              </div>\n            </div>\n\n            <div class=\'row\'>\n              <div class=\'input-field col s12\'>\n                <input class=\'validate no_margin\' type=\'text\' name=\'name\' id=\'name\' />\n                <label for=\'email\'>Enter your Name</label>\n              </div>\n            </div>\n\n            <div class=\'row\'>\n              <div class=\'input-field col s12\'>\n                <input class=\'validate no_margin\' type=\'email\' name=\'email\' id=\'email\' />\n                <label for=\'password\'>Enter your Email</label>\n              </div>\n            </div>\n\n            <div class=\'row\'>\n              <div class=\'input-field col s12\'>\n                <input class=\'validate no_margin\' type=\'password\' name=\'password\' id=\'password\' />\n                <label for=\'password\'>Enter your password</label>\n              </div>\n            </div>\n\n            <div class=\'row\'>\n              <div class=\'input-field col s12\'>\n                <input class=\'validate no_margin\'  type="text" name=\'university\' id=\'university\' />\n                <label for=\'university\'>Enter your University</label>\n              </div>\n            </div>\n\n            <br />\n            <center>\n              <div class=\'row\'>\n                <button type=\'submit\' name=\'btn_login\' class=\'col s12 btn btn-large waves-effect indigo\'>Register</button>\n              </div>\n            </center>\n          </form>\n        </div>\n      </div>\n      <a href="/action/index" class="white-text">Aleady have an account? <span class="button-underlined">Login</span></a>\n    </center>\n\n    <!-- <div class="section"></div> -->\n  </main>\n\n  <script src="/js/jquery-2.1.1.min.js"></script>\n  <script src="/js/materialize.js"></script>\n</body>\n\n</html>\n  \n  \n</body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"17": 0, "28": 22, "22": 1}, "uri": "/signup.html", "filename": "/home/mayur/Researchforum/Researchforum/researchforum/templates/signup.html"}
__M_END_METADATA
"""
