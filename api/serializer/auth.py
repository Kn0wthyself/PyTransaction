# -*- coding: utf8 -*-
from django.db.models import Q
from rest_framework import serializers
from rest_framework_jwt.compat import PasswordField, Serializer
from rest_framework_jwt.settings import api_settings
from django.utils.translation import ugettext as _
from django.contrib.auth.models import User

from api.models import Profile

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_decode_handler = api_settings.JWT_DECODE_HANDLER
jwt_get_username_from_payload = api_settings.JWT_PAYLOAD_GET_USERNAME_HANDLER


class JSONWebTokenSerializer(Serializer):

    def __init__(self, *args, **kwargs):
        super(JSONWebTokenSerializer, self).__init__(*args, **kwargs)

        self.fields['username'] = serializers.CharField()
        self.fields['password'] = PasswordField(write_only=True)

    def validate(self, attrs):
        username = attrs.get('username')
        try:
            profile = Profile.objects.get(Q(nickname=username) |
                                          Q(email=username) |
                                          Q(mobile=username))
            user = profile.user
        except Profile.DoesNotExist:
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                msg = _('check your username is correct?')
                raise serializers.ValidationError(msg)

        if user.check_password(attrs.get('password')):
            payload = jwt_payload_handler(user)
            return {'token': jwt_encode_handler(payload), 'user': user}
        else:
            msg = _('password is not correct.')
            raise serializers.ValidationError(msg)




class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def save(self, **kwargs):
        data = self.data
        user = User.objects.create(username=data.get('username'),
                                   email=data.get('email'))
        user.set_password(data.get('password'))
        user.save()
        Profile.objects.create(user=user,
                               nickname=data.get('username'),
                               mobile=data.get('username'),
                               email=data.get('email'))
        return user

class PasswordSerializer(Serializer):

    def __init__(self, *args, **kwargs):
        super(PasswordSerializer, self).__init__(*args, **kwargs)

        self.fields['username'] = serializers.CharField()
        self.fields['password'] = PasswordField(write_only=True)

    def validate(self, attrs):
        username = attrs.get('username')
        try:
            profile = Profile.objects.get(Q(nickname=username) |
                                          Q(email=username) |
                                          Q(mobile=username))
            user = profile.user
        except Profile.DoesNotExist:
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                msg = _('check your username is correct?')
                raise serializers.ValidationError(msg)
        print(attrs.get('password'))
        user.set_password(attrs.get('password'))
        user.save()
        if user.check_password(attrs.get('password')):
            return {'msg': 'success'}
        else:
            msg = _('password change failed.')
            raise serializers.ValidationError(msg)



