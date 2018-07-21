#!/usr/bin/env python
# encoding: utf-8

"""
@version: 1.0
@author: Jervon
@contact: jervon@foxmail.com
@time: 2018/4/23 上午9:51
"""

import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options
from tornado.options import define, options
from common.settings import settings
from urls import urls

define("port", default=9001, type=int)
if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application(urls,
        debug=settings['DEBUG']
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()