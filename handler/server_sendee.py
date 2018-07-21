#!/usr/bin/env python
# encoding: utf-8

"""
@version: 1.0
@author: Jervon
@contact: jervon@foxmail.com
@time: 2018/5/8 下午2:58
"""

from common.jsondump import JsonDump
from tornado import gen, web
from celery_service.proj.tasks import test_01
from celery_service.proj.celery_app import app


class ServerSendeeHandler(JsonDump):
    """
    后端统一接收
    """
    def get(self):
        self.tasked()
        self.json_success()

    @gen.coroutine
    def tasked(self):
        print("处理任务")
        test_01.apply_async((1,2))


class CeleryTaskDoneHandler(JsonDump):
    """
    celery处理结果
    """
    def post(self, *args, **kwargs):
        print("结果接收处理")
        self.json_success(message='结果接收处理')