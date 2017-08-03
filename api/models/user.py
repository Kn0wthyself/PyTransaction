from django.db import models
from django.contrib.auth.models import User

from .base import BaseModel


class Profile(BaseModel):
    """
    用户基本信息
    """
    user = models.OneToOneField(User, related_name='profile')
    nickname = models.CharField('昵称', max_length=64, unique=True)
    mobile = models.CharField('手机', max_length=11, unique=True)
    email = models.CharField('邮箱', max_length=128, unique=True)
    head_photo = models.CharField('头像', max_length=256, default='', blank=True)
    sex = models.CharField('性别', max_length=1, choices=(('m', u'男'), ('f', u'女')), default='', blank=True)
    birth = models.DateField('生日', null=True, blank=True)
    wechat = models.CharField('微信号', max_length=64, default='', blank=True)
    qq = models.CharField('QQ号', max_length=20, default='', blank=True)


class DeveloperProfile(BaseModel):
    """
    开发者信息
    """
    user = models.OneToOneField(User, related_name='dev_profile')
    github = models.CharField('github帐号', max_length=64, default='', blank=True)
    skill = models.CharField('技能', max_length=256, default='', blank=True)
    introduction = models.TextField('自我介绍', default='', blank=True)


class EmployerProfile(BaseModel):
    """
    雇主信息
    """
    user = models.OneToOneField(User, related_name='emp_profile')

