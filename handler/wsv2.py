#!/usr/bin/env python
# encoding: utf-8

"""
    ws的json格式
@version: 1.0
@author: Jervon
@contact: jervon@foxmail.com
@time: 2018/5/3 上午9:15
"""
import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options
from tornado.websocket import WebSocketHandler
from tornado import gen
import asyncio
from urllib.parse import urlparse
from common.settings import settings


class wsVersionTwoHandler(WebSocketHandler):
    def open(self):
        pass

    def on_message(self, message):
        self.write_message("测试")

    def on_close(self):
        pass