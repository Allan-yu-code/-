from rest_framework.views import APIView
from django.conf import settings
from urllib.parse import urlencode
from urllib.request import urlopen
from rest_framework.response import Response
import json
import logging
log = logging.getLogger("django")
# Create your views here.
class CaptchaAPIView(APIView):
    def get(self,request):
        """验证码验证接口"""
        AppSecretKey = settings.TENCENT_CAPTCHA.get("App_Secret_Key")
        appid = settings.TENCENT_CAPTCHA.get("APPID")
        Ticket = request.query_params.get("ticket")
        Randstr = request.query_params.get("randstr")
        # 获取客户端的IP地址
        UserIP = request._request.META.get("REMOTE_ADDR")
        params = {
            "aid": appid,
            "AppSecretKey": AppSecretKey,
            "Ticket": Ticket,
            "Randstr": Randstr,
            "UserIP": UserIP
        }
        params = urlencode(params)
        ret = self.txrequest(params)
        return Response({"message":ret})

    def txrequest(self, params):
        url = settings.TENCENT_CAPTCHA.get("GATEWAY")
        content = urlopen("%s?%s" % (url, params)).read()
        res = json.loads(content)
        try:
            return res["response"] == "1"
        except:
            log.error( "验证码错误，%s:%s" % (res["response"], res["err_msg"]) )
            return False

from rest_framework.generics import CreateAPIView
from .models import User
from .serializers import UserModelSerializer
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action
from rest_framework import status
import re
class UserAPIView(GenericViewSet,CreateAPIView):
    """用户视图接口"""
    queryset = User.objects.all()
    serializer_class = UserModelSerializer

    @action(methods=["get"],detail=False)
    def mobile(self,request):
        """验证手机号的唯一性"""
        mobile = request.query_params.get("mobile")
        if not re.match("^1[3-9]\d{9}$",mobile):
            return Response({"message":"手机号码格式有误！"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            User.objects.get(mobile=mobile)
            return Response({"message":"手机号已经被注册！"}, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({"message":"手机号可以注册使用！"}, status=status.HTTP_200_OK)

from renranapi.libs.yuntongxun.sms import CCP
from django_redis import get_redis_connection
from django.conf import settings
from renranapi.settings import constants
import random
import logging
loger = logging.getLogger("django")
class SMSCodeAPIView(APIView):
    """
    短信验证码
    """
    def get(self,request, mobile):
        # todo 0. 短信发送间隔判断
        redis_conn = get_redis_connection("sms_code")
        interval = redis_conn.ttl("interval_%s" % mobile) # 如果数据过期了，则值为-2
        if interval > -1:
            return Response({"message":"对不起，发送短信频繁，请在%d秒再次点击发送！" % interval},status=status.HTTP_400_BAD_REQUEST)

        # 1. 生成验证码
        sms_code = "%05d" % random.randint(0,99999)
        # 2. 保存验证码到redis中
        redis_conn.setex( "sms_%s" % mobile, constants.SMS_EXPIRE_TIME, sms_code )
        redis_conn.setex( "interval_%s" % mobile, constants.SMS_INTERVAL_TIME,"_")
        # 3. 发送验证码
        ccp = CCP()
        ret = ccp.send_template_sms(mobile,[sms_code,constants.SMS_EXPIRE_TIME//60], settings.SMS["_templateID"])
        if not ret:
            loger.error("发送短信失败！用户:%s" % mobile )

        # 4. 返回响应信息
        return Response({"message":"短信已经发送，请留意您的手机短信！"})