from django.db import models
from django.contrib.auth.models import User

from api.models.base import BaseModel
from api.models.post import Post


STATUS = ((100, '待付款'), (200, '已取消'), (300, '已付款'))


class Order(BaseModel):
    amount = models.DecimalField('订单金额', max_digits=10, decimal_places=2)
    pay_user = models.ForeignKey(User, verbose_name='付款人')
    receive_user = models.ForeignKey(User, verbose_name='收款人')
    title = models.CharField('商品名称', max_length=64)
    status = models.IntegerField('订单状态', choices=STATUS)
    post = models.ForeignKey(Post, verbose_name='关联帖子')
