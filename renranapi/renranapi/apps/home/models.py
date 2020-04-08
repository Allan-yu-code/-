from django.db import models
from renranapi.utils.models import BaseModel
# Create your models here.
class Banner(BaseModel):
    """
    轮播图
    """
    # upload_to 存储子目录，真实存放地址会使用配置中的MADIE_ROOT+upload_to
    image = models.ImageField(upload_to='banner', verbose_name='轮播图', null=True,blank=True)
    note = models.CharField(null=True, blank=True, max_length=150, verbose_name='备注信息')
    link = models.CharField(null=True, blank=True, max_length=150, verbose_name='轮播图广告地址', help_text="站内地址格式：/users/<br>站外地址格式：http://www.baidu.com")
    start_time = models.DateTimeField(verbose_name="上架时间",default=None, null=True, blank=True)
    end_time = models.DateTimeField(verbose_name="下架时间",default=None, null=True, blank=True)
    is_http = models.BooleanField(verbose_name="是否站外地址", default=False)

    class Meta:
        db_table = 'rr_banner'
        verbose_name = '轮播图'
        verbose_name_plural = verbose_name

class Nav(BaseModel):
    """导航菜单"""
    POSITION = (
        (1, "头部导航"),
        (2, "脚部导航"),
    )
    pid = models.ForeignKey("Nav", related_name="son", null=True, blank=True, on_delete=models.DO_NOTHING, verbose_name="父亲导航", )
    link = models.CharField(max_length=500, verbose_name='导航地址', help_text="如果是站外链接,必须加上协议, 格式如: http://www.renran.cn")
    is_http = models.BooleanField(verbose_name="是否站外地址", default=False)
    option = models.SmallIntegerField(choices=POSITION, default=1, verbose_name="导航位置")

    class Meta:
        db_table = 'rr_nav'
        verbose_name = '导航菜单'
        verbose_name_plural = verbose_name

    @property
    def son_list(self):
        """子导航列表"""
        try:
            result = self.son.filter(is_show=True, is_delete=False).order_by("orders", "-id")[:8]
        except:
            result = []

        data = []
        for nav in result:
            data.append({
                "name": nav.name,
                "link": nav.link,
                "is_http": nav.is_http,
            })
        return data