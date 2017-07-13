# -*- coding: utf8 -*-
from django.db import models
from django.contrib.auth.models import User

from api.models.base import BaseModel


STATUS = ((100, '未发布'), (200, '待接单'), (300, '已接单'), (400, '已完成'), (500, '已关闭'))


class Post(BaseModel):
    """
    需求贴
    """
    author = models.ForeignKey(User, verbose_name='发帖人')
    title = models.CharField('标题', max_length=256)
    content = models.TextField('内容')
    reward = models.DecimalField('报酬', max_digits=10, decimal_places=2)
    contact_mobile = models.CharField('联系号码', max_length=11)
    status = models.IntegerField(verbose_name='帖子状态', choices=STATUS)


class Tag(BaseModel):
    """
    标签
    """
    name = models.CharField('标签名', max_length=20)


class PostTag(BaseModel):
    """
    帖子标签
    """
    post = models.ForeignKey(Post, verbose_name='帖子')
    tag = models.ForeignKey(Tag, verbose_name='标签')
