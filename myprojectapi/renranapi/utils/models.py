from django.db import models
class BaseModel(models.Model):
    """公共模型"""
    name = models.CharField(null=True, default="暂无", blank=True, max_length=150, verbose_name='名称')
    orders = models.IntegerField(default=0, verbose_name='显示顺序')
    is_show = models.BooleanField(default=False, verbose_name="是否上架")
    is_delete = models.BooleanField(default=False, verbose_name="逻辑删除")
    created_time = models.DateTimeField(null=True,blank=True, auto_now_add=True, verbose_name="添加时间")
    updated_time = models.DateTimeField(null=True,blank=True, auto_now=True, verbose_name="更新时间")

    class Meta:
        # 设置当前模型在数据迁移的时候不要为它创建表
        abstract = True

    def __str__(self):
        return self.name if self.name else ""