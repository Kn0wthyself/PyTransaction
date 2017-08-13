from django.db import models
from django.contrib.auth.models import User

from api.models.base import BaseModel


STATUS = ((100, '未发布'), (200, '待接单'), (300, '已接单'), (400, '已完成'), (500, '已关闭'))

class Tag(BaseModel):
    """
    标签
    """
    name = models.CharField('标签名', max_length=20)

class Post(BaseModel):
    """
    需求贴
    """
    author = models.ForeignKey(User, verbose_name='发帖人')
    author_nickname = models.CharField('发布者昵称', null=True, blank=True, max_length=256)
    developer = models.ForeignKey(User, verbose_name='开发者', null=True, blank=True, on_delete=models.CASCADE)
    developer_nickname = models.CharField('开发者昵称', null=True, blank=True, max_length=256)
    title = models.CharField('标题', max_length=256)
    content = models.TextField('内容')
    reward = models.DecimalField('报酬', max_digits=10, decimal_places=2)
    contact_mobile = models.CharField('联系号码', max_length=11)
    status = models.IntegerField(verbose_name='帖子状态', choices=STATUS)
    tag = models.ForeignKey(Tag, null=True, blank=True, on_delete=models.CASCADE, verbose_name='标签')

# class PostTag(BaseModel):
#     """
#     帖子标签
#     """
#     post = models.ForeignKey(Post, verbose_name='帖子')
#     tag = models.ForeignKey(Tag, verbose_name='标签')
