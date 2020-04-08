from mycelery.main import app
from celery.app.task import Task
from .yuntongxun.sms import CCP
from renranapi.settings import constants
from django.conf import settings
import logging
loger = logging.getLogger("django")

class Mytask(Task):
    """任务的监听器"""
    def on_success(self, retval, task_id, args, kwargs):
        print('task success')
        return super(Mytask, self).on_success(retval, task_id, args, kwargs)

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        print('task failed')
        return super(Mytask, self).on_failure(exc, task_id, args, kwargs, einfo)

    def after_return(self, status, retval, task_id, args, kwargs, einfo):
        print('this is after return')
        return super(Mytask, self).after_return(status, retval, task_id, args, kwargs, einfo)

    def on_retry(self, exc, task_id, args, kwargs, einfo):
        print('this is retry')
        return super(Mytask, self).on_retry(exc, task_id, args, kwargs, einfo)

@app.task(name="send_sms", base=Mytask)
def send_sms(mobile, sms_code):
    ccp = CCP()
    ret = ccp.send_template_sms(mobile, [sms_code, constants.SMS_EXPIRE_TIME // 60], settings.SMS["_templateID"])
    if not ret:
        loger.error("发送短信失败！用户:%s" % mobile)