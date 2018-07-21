#!/usr/bin/env python
# encoding: utf-8

"""
@version: 1.0
@author: Jervon
@contact: jervon@foxmail.com
@time: 2018/5/10 下午5:15
"""


from multiprocessing import cpu_count
from celery import platforms
from kombu import Exchange, Queue, binding
import os, sys

base_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(base_path)
from common.settings import settings


CELERYD_POOL_RESTARTS = False # 不关闭缓存，返回worker执行的结果
CELERY_INCLUDE = 'proj.tasks'
BROKER_URL = settings.get("redis_url")
CELERY_RESULT_BACKEND = settings.get("redis_url") # 返回结果到redis
CELERY_IMPORTS = ['proj.tasks']

CELERY_DEFAULT_QUEUE = 'default'
CELERY_DEFAULT_EXCHANGE = 'default'
CELERY_DEFAULT_EXCHANGE_TYPE = 'direct'
CELERY_DEFAULT_ROUTING_KEY = 'default'
# CELERY_MESSAGE_COMPRESSION = 'gzip'
CELERY_ACKS_LATE = True     # 可以让你的Celery更加可靠，只有当worker执行完任务后，才会告诉MQ，消息被消费。
CELERYD_PREFETCH_MULTIPLIER = 1
# CELERY_DISABLE_RATE_LIMITS = True   # 对任务消费的速率进行限制，关掉可加速
CELERY_TIMEZONE = 'Asia/Shanghai'
CELERY_ENABLE_UTC = True
# CELERYD_CONCURRENCY = cpu_count() // 2
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_PUBLISH_RETRY = True
CELERY_TASK_PUBLISH_RETRY_POLICY = {
    'max_retries': 3,
    'interval_start': 10,
    'interval_step': 5,
    'interval_max': 20
}
platforms.C_FORCE_ROOT = True

