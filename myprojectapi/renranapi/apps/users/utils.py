def jwt_response_payload_handler(token, user=None, request=None):
    """jwt自定义响应载荷"""
    return {
        "token":token,
        'id': user.id,
        'username': user.username,
        'avatar': user.avatar.url if user.avatar else "",
        'nickname': user.nickname if user.nickname else "",
    }

from django.contrib.auth import get_user_model
from django.db.models import Q
def get_user_by_account(account):
    """
    通过账户信息获取用户模型
    :param account: 可以是username,也可以手机号或者邮箱,获取其他的唯一字段信息
    :return: user模型
    """
    User = get_user_model()
    try:
        return User.objects.get(Q(mobile=account) | Q(username=account) | Q(email=account))
    except User.DoesNotExist:
        return None


from django.contrib.auth.backends import ModelBackend
class AccountModelBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        user = get_user_by_account(username)
        if user is not None and user.check_password(password) and self.user_can_authenticate(user):
            return user