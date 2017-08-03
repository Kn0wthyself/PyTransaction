from django.db.models import Q
from rest_framework import serializers
from rest_framework_jwt.compat import PasswordField, Serializer
from rest_framework_jwt.settings import api_settings
from django.utils.translation import ugettext as _
from django.contrib.auth.models import User

from api.models import Profile
from api.models.transaction import Order
from api.models.post import Post, PostTag

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_decode_handler = api_settings.JWT_DECODE_HANDLER
jwt_get_username_from_payload = api_settings.JWT_PAYLOAD_GET_USERNAME_HANDLER

class PostTagSerializer(serializers.ModelSerializer):

    class Meta:
        model = PostTag
        fields = ('author', 'title', 'content', 'reward', 'contact_mobile', 'status', 'tag')

    def save(self, **kwargs):
        data = self.data
        posttag = PostTag.objects.create(author=data.get('author'),
                                         title=data.get('title'),
                                         content=data.get('content'),
                                         reward=data.get('reward'),
                                         contact_mobile=data.get('contact_mobile'),
                                         status=data.get('status'),
                                         tag=data.get('tag'))
        return posttag


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ('amount', 'pay_user', 'title', 'status', 'post')

    def save(self, **kwargs):
        data = self.data
        order = Order.objects.create(amount=data.get('amount'),
                                     pay_user=data.get('pay_user'),
                                     receive_user=data.get('receive_user'),
                                     title=data.get('title'),
                                     status=data.get('status'),
                                     post=data.get('post'))
        return order
