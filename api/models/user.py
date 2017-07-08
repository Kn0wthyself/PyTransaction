# -*- coding: utf8 -*-
from django.db import models
from django.contrib.auth.models import User

from .base import BaseModel


class Profile(BaseModel):
    """
    用户基本信息
    """
    user = models.OneToOneField(User, related_name='profile')
    nickname = models.CharField(u'昵称', max_length=64, unique=True)
    mobile = models.CharField(u'手机', max_length=11, unique=True)
    email = models.CharField(u'邮箱', max_length=128, unique=True)
    sex = models.CharField(u'性别', max_length=1, choices=(('m', u'男'), ('f', u'女')), default='', blank=True)
    birth = models.DateField(u'生日', null=True, blank=True)
    wechat = models.CharField(u'微信号', max_length=64, default='', blank=True)
    qq = models.CharField(u'QQ号', max_length=20, default='', blank=True)


class DeveloperProfile(BaseModel):
    """
    开发者信息
    """
    user = models.OneToOneField(User, related_name='dev_profile')
    github = models.CharField(u'github帐号', max_length=64, default='', blank=True)
    skill = models.CharField(u'技能', max_length=256, default='', blank=True)
    introduction = models.TextField(u'自我介绍', default='', blank=True)


class EmployerProfile(BaseModel):
    """
    雇主信息
    """
    user = models.OneToOneField(User, related_name='emp_profile')

