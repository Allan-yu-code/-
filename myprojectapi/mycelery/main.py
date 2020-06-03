# Celery入口文件/主程序
from celery import Celery
# 初始化celery实例对象
app = Celery("renran")

# 如果和第三方框架进行组合使用，需要在这里编写整合的代码
import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'renranapi.settings.dev')
django.setup()

# 加载配置信息
app.config_from_object("mycelery.config")

# 注册任务
app.autodiscover_tasks(["mycelery.sms","mycelery.article"])

# 最后在终端下启动celery，就会自动跑到任务队列中读取任务，并执行
# celery -A mycelery.main worker --loglevel=info