from django.db import models
from renranapi.utils.models import BaseModel
from users.models import User
class OAuthUser(BaseModel):
    """
    QQ登录用户数据
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户')
    openid = models.CharField(max_length=64, verbose_name='openid', db_index=True)
    access_token = models.CharField(max_length=500,verbose_name="临时访问票据", help_text="有效期:3个月")
    refresh_token = models.CharField(max_length=500,verbose_name="刷新访问票据的token", help_text="当access_token以后,可以使用refresh_token来重新获取新的access_token")

    class Meta:
        db_table = 'rr_oauth_qq'
        verbose_name = 'QQ登录用户数据'
        verbose_name_plural = verbose_name