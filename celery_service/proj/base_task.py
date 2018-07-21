#!/usr/bin/env python
# encoding: utf-8

"""
@version: 1.0
@author: Jervon
@contact: jervon@foxmail.com
@time: 2018/5/16 下午4:07
"""


import json
import requests
from celery.app.task import Task
from proj import *


class BaseTask(Task):
    def on_success(self, retval, task_id, args, kwargs):
        site_url = settings.get("site_url")
        url = "{site_url}/celery_task_done/".format(site_url=site_url)
        data = {}
        data['test'] = json.dumps(retval)
        res = requests.post(url=url, data=data)
        print("任务处理结果rpc")
        # print("res=", res.text)
        return super(BaseTask, self).on_success(retval, task_id, args, kwargs)

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        print('task fail, reason: {0}'.format(exc))
        return super(BaseTask, self).on_failure(exc, task_id, args, kwargs, einfo)