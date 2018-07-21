#!/usr/bin/env python
# encoding: utf-8

"""
@version: 1.0
@author: Jervon
@contact: jervon@foxmail.com
@time: 2018/4/24 下午2:27
"""

import os, sys
import pytz


BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

CELERY_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/celery_service"
sys.path.append(CELERY_ROOT)

settings = dict()
settings['BASE_DIR'] = BASE_DIR
settings['DEBUG'] = True

tz = pytz.timezone('Asia/Shanghai')
settings['site_url'] = "http://127.0.0.1:9001"
settings['redis_url'] = "redis://@127.0.0.1:6379/0"