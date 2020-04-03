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