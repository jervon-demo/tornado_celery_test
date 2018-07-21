# 项目介绍
Tonrado + Celery实现后端异步处理任务

# 项目目录

. 项目根目录
├── celery_service	# celery目录
│   ├── celeryconfig.py	# celery配置文件
│   ├── proj
│   │   ├── base_task.py		# task
│   │   ├── celery_app.py	# celery启动
│   │   └── tasks.py
│   └── service
│       └── task_done.py	# task处理结果接收
├── common
│   ├── jsondump.py	# json输出格式化
│   └── settings.py	# Tornado配置文件
├── handler
│   ├── server_sendee.py	# 生产task、task结果处理
│   └── wsv2.py	# WebSocket
├── requirements.txt
├── tornado_app.py	# tornado启动
└── urls.py	# tornado路由


# 安装
## redis
```
$ wget http://download.redis.io/releases/redis-4.0.9.tar.gz
$ tar xzf redis-4.0.9.tar.gz
$ cd redis-4.0.9
$ make
$ src/redis-server
```

## 下载demo
```
git clone ...
pip install -r requirements.txt
```

# 运行
```
cd tornado_celery_test
# 启动Tornado
python tornado_app.py

cd celery_service/
# 启动celery应用
celery -A proj worker -l info
# 启动flower
celery flower -A proj
```

# 生产/消费task
浏览器访问：http://127.0.0.1:9001/service_sendee/

# 效果
![](http://images.zengjianfeng.com/2018-05-30-celery_demo.gif)



