from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from .utils import OAuthQQ,QQNetWorkError,QQDataError
from .models import OAuthUser
from users.utils import get_user_by_account
from rest_framework.decorators import action
from users.models import User
class OAuthQQUserAPIView(ViewSet):
    """QQ第三方登录视图接口"""
    def get_url(self,request):
        """提供QQ登录的url地址"""
        auth = OAuthQQ()
        url = auth.qq_login_url()
        return Response(url)

    def get_info(self,request):
        # 1. 接受客户端转发的授权码
        code = request.query_params.get("code")
        auth = OAuthQQ()
        try:
            # 2. 通过授权码获取临时票据
            access_token,refresh_token = auth.get_access_token(code)
            # 3. 通过临时票据获取openID
            openid = auth.get_open_id(access_token)
            # 4F65D2442D41B0D1639FD7FC14123B11

        except QQNetWorkError:
            return Response({"message":"网络异常，QQ第三方登录失败！"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except QQDataError:
            return Response({"message":"数据异常，QQ第三方登录失败！"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
            return Response({"message":"未知异常，QQ第三方登录失败！"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        # 判断用户是否是第一次使用QQ登录
        try:
            qq_user = OAuthUser.objects.get(openid=openid)
            user = qq_user.user
            # 用户非第一次使用QQ登录，直接保存登录状态，返回jwt
            from rest_framework_jwt.settings import api_settings
            jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
            jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

            payload = jwt_payload_handler(user)
            token = jwt_encode_handler( payload )
            return Response({
                "token": token,
                'id': user.id,
                'username': user.username,
                'avatar': user.avatar.url if user.avatar else "",
                'nickname': user.nickname if user.nickname else "",
            })

        except OAuthUser.DoesNotExist:
            # 用户属于第一次使用QQ登录，进入账号绑定页面，需要返回open和access_token等信息返回给客户端
            return Response({
                "openid": openid,
                "access_token":access_token,
                "refresh_token":refresh_token,
            })

    @action(methods=["put"], detail=False)
    def qq_login(self,request):
        """网站用户初次使用QQ登录"""
        username = request.data.get("username")
        password = request.data.get("password")
        openid   = request.data.get("openid")
        access_token   = request.data.get("access_token")
        refresh_token  = request.data.get("refresh_token")

        user = get_user_by_account(username)
        if user is None:
            return Response({"message":"对不起，用户不存在！"}, status=status.HTTP_400_BAD_REQUEST)

        # 验证密码
        if not user.check_password(password):
            return Response({"message": "对不起，账号或密码错误！"}, status=status.HTTP_400_BAD_REQUEST)

        # 把用户和openID进行绑定
        try:
            OAuthUser.objects.create(
                user=user,
                openid=openid,
                access_token=access_token,
                refresh_token=refresh_token,
            )
        except:
            return Response({"message":"对不起，QQ账号绑定失败!"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        # 用户非第一次使用QQ登录，直接保存登录状态，返回jwt
        from rest_framework_jwt.settings import api_settings
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        return Response({
            "token": token,
            'id': user.id,
            'username': user.username,
            'avatar': user.avatar.url if user.avatar else "",
            'nickname': user.nickname if user.nickname else "",
        })

    @action(methods=["post"], detail=False)
    def qq_register(self,request):
        """游客使用QQ登录完成注册过程"""
        nickname = request.data.get("nickname")
        mobile = request.data.get("mobile")
        sms_code = request.data.get("sms_code")
        password = request.data.get("password")
        openid   = request.data.get("openid")
        access_token   = request.data.get("access_token")
        refresh_token  = request.data.get("refresh_token")

        # todo 验证数据

        try:
            user = User.objects.create_user(
                nickname=nickname,
                username=mobile,
                mobile=mobile,
                password=password,
            )
        except:
            return Response({"message": "QQ账号注册失败!"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        # QQ和新账号的绑定关系
        try:
            OAuthUser.objects.create(
                user=user,
                openid=openid,
                access_token=access_token,
                refresh_token=refresh_token,
            )
        except:
            return Response({"message":"对不起，QQ账号绑定失败!"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        # 用户非第一次使用QQ登录，直接保存登录状态，返回jwt
        from rest_framework_jwt.settings import api_settings
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        return Response({
            "token": token,
            'id': user.id,
            'username': user.username,
            'avatar': user.avatar.url if user.avatar else "",
            'nickname': user.nickname if user.nickname else "",
        })