from rest_framework import serializers
from django.contrib.auth.models import User

from api.models.transaction import Order
from api.models.post import Post, Tag

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('id','author', 'title', 'content', 'reward', 'contact_mobile', 'status', 'tag')

    def save(self, **kwargs):
        data = self.data
        post = Post.objects.create(author=User.objects.get(id=data.get('author')),
                                    title=data.get('title'),
                                    content=data.get('content'),
                                    reward=data.get('reward'),
                                    contact_mobile=data.get('contact_mobile'),
                                    status=data.get('status'),
                                    tag=Tag.objects.get(id=data.get('tag')))
        return post


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ('amount', 'pay_user', 'receive_user', 'title', 'status', 'post')

    def save(self, **kwargs):
        data = self.data
        order = Order.objects.create(amount=data.get('amount'),
                                     pay_user=User.objects.get(id=data.get('pay_user')),
                                     receive_user=User.objects.get(id=data.get('receive_user')),
                                     title=data.get('title'),
                                     status=data.get('status'),
                                     post=Post.objects.get(id=data.get('post')))
        return order
