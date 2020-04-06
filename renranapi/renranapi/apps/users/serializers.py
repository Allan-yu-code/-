from rest_framework import serializers
from .models import User
import re
class UserModelSerializer(serializers.ModelSerializer):
    """用户信息序列化器"""
    # 1. 字段声明
    sms_code = serializers.CharField(write_only=True,max_length=5, min_length=5, help_text="短信验证码",label="短信验证码")
    token = serializers.CharField(read_only=True, help_text="jwt", label="jwt")
    # 2. Meta声明
    class Meta:
        model = User
        # fields里面没有在模型中进行声明的字段，都需要在序列化器中单独声明
        fields = ["id","nickname","username","mobile","avatar","password","sms_code","token"]
        extra_kwargs = {
            "nickname":{
                "required":True,
                "error_messages":{
                    "required":"对不起，用户昵称不能为空！",
                }
            },
            "password":{"write_only":True,"max_length":16,"min_length":6,"required":True},
            "mobile":{"write_only":True,"required":True},
            "username":{"read_only":True,},
            "avatar":{"read_only":True,}
        }

    # 3. 验证方法
    def validate(self, attrs):
        # todo 作业： 验证昵称是否被使用了

        # 1. 验证手机格式是否正确
        mobile = attrs.get("mobile")
        if not re.match("^1[3-9]\d{9}$",mobile):
            raise serializers.ValidationError("手机号码格式有误!")

        # 验证手机号是否已经注册了
        try:
            User.objects.get(mobile=mobile)
            raise serializers.ValidationError("对不起，手机号已经被注册！")
        except User.DoesNotExist:
            pass

        # todo 短信验证码的校验

        return attrs

    # 4. 数据库操作
    def create(self, validated_data):
        try:
            user = User.objects.create_user(
                username=validated_data.get("mobile"),
                nickname=validated_data.get("nickname"),
                mobile=validated_data.get("mobile"),
                password=validated_data.get("password"),
            )
        except:
            raise serializers.ValidationError("注册用户信息失败！")

        from rest_framework_jwt.settings import api_settings
        # 首次注册,免登录,手动生成jwt
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(user)
        user.token = jwt_encode_handler(payload)
        return user