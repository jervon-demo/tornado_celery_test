#!/usr/bin/env python
# encoding: utf-8

"""
@version: 1.0
@author: Jervon
@contact: jervon@foxmail.com
@time: 2018/5/10 下午4:26
"""

from __future__ import absolute_import, unicode_literals
from celery import Celery
# from proj import *
import os,sys
# from proj.test_002 import *


base_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(base_path)
from common.settings import settings


app = Celery(
    'proj'
             # broker=settings.get("redis_url"),
             # backend='amqp://',
             # include=['proj.tasks']
)

# Optional configuration, see the application user guide.
app.conf.update(
    result_expires=3600,
)
app.config_from_object('celeryconfig')

if __name__ == '__main__':
    app.start()