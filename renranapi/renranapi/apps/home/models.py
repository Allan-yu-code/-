from django.db import models

# Create your models here.
class Banner(models.Model):
    """
    轮播图
    """
    # upload_to 存储子目录，真实存放地址会使用配置中的MADIE_ROOT+upload_to
    image = models.ImageField(upload_to='banner', verbose_name='轮播图', null=True,blank=True)
    name = models.CharField(max_length=150, verbose_name='轮播图名称')
    note = models.CharField(null=True, blank=True, max_length=150, verbose_name='备注信息')
    link = models.CharField(null=True, blank=True, max_length=150, verbose_name='轮播图广告地址')
    start_time = models.DateTimeField(verbose_name="上架时间",default=None, null=True, blank=True)
    end_time = models.DateTimeField(verbose_name="下架时间",default=None, null=True, blank=True)
    orders = models.IntegerField(default=0, verbose_name='显示顺序')
    is_http = models.BooleanField(verbose_name="是否站外地址", default=False, help_text="站内地址格式：/users/<br>站外地址格式：http://www.baidu.com")
    is_show=models.BooleanField(default=False, verbose_name="是否上架")
    is_delete=models.BooleanField(default=False, verbose_name="逻辑删除")

    class Meta:
        db_table = 'rr_banner'
        verbose_name = '轮播图'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name