from django.conf import settings
from urllib.parse import urlencode,parse_qs
from urllib.request import urlopen
import logging,json
logger = logging.getLogger("django")

class QQDataError(Exception):
    pass

class QQNetWorkError(Exception):
    pass

class OAuthQQ(object):
    """QQ登录辅助类"""
    def __init__(self, *args, **kwargs):
        """配置初始化"""
        self.app_id = kwargs.get("app_id", settings.QQ_APP_ID)
        self.app_key = kwargs.get("app_key", settings.QQ_APP_KEY)
        self.redirect_url = kwargs.get("redirect_url", settings.QQ_REDIRECT_URL)
        self.state = kwargs.get("state", settings.QQ_STATE)

    def qq_login_url(self):
        """获取QQ第三方登录地址"""
        url = "https://graph.qq.com/oauth2.0/authorize?"
        params = {
            "response_type": "code",
            "client_id": self.app_id,
            "redirect_uri": self.redirect_url,
            "state": self.state,
        }

        return url + urlencode(params)

    def get_access_token(self,code):
        """通过授权码获取临时票据"""
        url = "https://graph.qq.com/oauth2.0/token?"
        params = {
            'grant_type': 'authorization_code',
            'client_id': self.app_id,
            'client_secret': self.app_key,
            'redirect_uri': self.redirect_url,
            'code': code,
        }
        # urlencode 把字典转换成查询字符串的格式
        url = 'https://graph.qq.com/oauth2.0/token?' + urlencode(params)

        try:
            response = urlopen(url)
            response_data = response.read().decode()
            data = parse_qs(response_data)
        except:
            logger.error('网络异常，QQ第三方登录失败！')
            raise QQNetWorkError

        try:
            # parse_qs　把查询字符串格式的内容转换成字典[注意：转换后的字典，值是列表格式]
            access_token = data.get('access_token')[0]
            refresh_token = data.get('refresh_token')[0]
        except:
            logger.error('code=%s msg=%s' % (data.get('code'), data.get('msg')))
            raise QQDataError

        return access_token,refresh_token

    def get_open_id(self,access_token):
        """通过临时票据获取openID"""
        url = 'https://graph.qq.com/oauth2.0/me?access_token=' + access_token

        try:
            response = urlopen(url)
            response_data = response.read().decode()
        except:
            logger.error('网络异常，QQ第三方登录失败！')
            raise QQNetWorkError

        try:
            data = json.loads(response_data[10:-4])
            openid = data.get('openid')
        except:
            logger.error('code=%s msg=%s' % (data.get('code'), data.get('msg')))
            raise QQDataError

        return openid

    def get_user_info(self,access_token,openid):
        """根据临时票据获取QQ用户的基本信息"""
        url = 'https://graph.qq.com/user/get_user_info?'
        params = {
            'access_token': access_token,
            'oauth_consumer_key': self.app_id,
            'openid': openid,
        }

        url+=urlencode(params)
        try:
            response = urlopen(url)
            response_data = response.read().decode()
        except:
            logger.error('网络异常，QQ第三方登录失败！')
            raise QQNetWorkError

        data = json.loads(response_data)
        return data