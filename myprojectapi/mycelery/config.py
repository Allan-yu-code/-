# 任务队列的链接地址
broker_url = 'redis://127.0.0.1:6379/15'
# 结果队列的链接地址
result_backend = 'redis://127.0.0.1:6379/14'
# 设置时区
from .main import app
from django.conf import settings
app.conf.timezone = settings.TIME_ZONE

# 定时任务调度器相关配置
from celery.schedules import crontab
app.conf.beat_schedule = {
    # 定时任务列表
    'pub-article-every-one-minute': {
        'task': 'interval_pub_article',  # 指定定时执行的的异步任务
        # 'schedule': crontab(),         # 时间间隔,一分钟
        'schedule': 10.0,               # 时间间隔,默认:秒
        # 'args': (16, 16)              # 如果任务有固定参数,则可以写在args
    },
}