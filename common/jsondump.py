#!/usr/bin/env python
# encoding: utf-8

"""
@version: 1.0
@author: Jervon
@contact: jervon@foxmail.com
@time: 2018/5/4 上午10:33
"""
from tornado.websocket import WebSocketHandler
import json
import tornado.web


class JsonDump(tornado.web.RequestHandler):
    def json_loads(self, data):
        return json.loads(data)

    def json_dumps(self, data):
        return json.dumps(data)

    def json_success(self, code=200 ,data={}, message='成功'):
        self.write(json.dumps({'code': code, 'data': data, 'message': message}))
        self.finish()

    def json_fail(self, code=501, data={}, message='失败'):
        # self.write_message({'code': code, 'data': data, 'message': message})
        self.write(json.dumps({'code': code, 'data': data, 'message': message}))
        self.finish()

    def json_error(self, code=500, data={}, message='错误'):
        result = {'code': code, 'data': data, 'message': message}
        if code:
            result['code'] = code
        self.write(json.dumps({'code': code, 'data': data, 'message': message}))
        self.finish()


