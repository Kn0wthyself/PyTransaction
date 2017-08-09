from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated

from api.serializer.auth import JSONWebTokenSerializer, UserSerializer
from api.serializer.post import OrderSerializer, PostSerializer
from api.models.user import EmployerProfile, DeveloperProfile
from api.models.post import Post, Tag
from api.models.transaction import Order

def GetUser(userid):
    user = User.objects.get(id=userid)
    return user

def GetTag(tagid):
    tag = Tag.objects.get(id=tagid)
    return tag

class GetMyOrdersAPI(generics.ListAPIView):
    '''
    返回当前用户所有的订单
    '''
    permission_classes = (IsAuthenticated,)
    serializer_class = PostSerializer
    def get_queryset(self):
        """
        This view should return a list of all the orders
        for the currently authenticated user.
        """
        user = self.request.user
        return Post.objects.filter(author_id=user.id)

class GetOnesOrdersAPI(generics.ListAPIView):
    '''
    返回某个用户对应的user_id所有的订单
    '''
    serializer_class = PostSerializer
    def get_queryset(self):
        """
        This view should return a list of all the orders for
        the user as determined by the user_id portion of the URL.
        """
        user_id = int(self.kwargs['user_id'])
        return Post.objects.filter(author_id=user_id)

class GetOrderByIdAPI(generics.ListAPIView):
    '''
    返回某个需求订单id所有的订单
    '''
    serializer_class = PostSerializer
    def get_queryset(self):
        """
        This view should return the order by the post_id portion of the URL.
        """
        post_id = int(self.kwargs['post_id'])
        return Post.objects.filter(id=post_id)

class GetAllOrdersAPI(generics.ListAPIView):
    '''
    返回所有用户对应的所有的订单
    '''
    serializer_class = PostSerializer
    def get_queryset(self):
        """
        This view should return a list of all the orders for
        all the user.
        """
        return Post.objects.all()

class CreatePostAPI(APIView):
    '''
    发表需求帖.
    '''
    permission_classes = (IsAuthenticated,)
    @classmethod
    def post(cls, request):
        data = request.data
        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            posttag = serializer.save()
            return Response(data={'msg': 'success'}, status=200)
        return Response(data={'error_msg': serializer.errors}, status=400)


class AcceptPostAPI(APIView):
    '''
    接受订单.
    '''
    permission_classes = (IsAuthenticated,)
    @classmethod
    def post(cls, request):
        '''
        通过需求贴ID定位需求帖.
        '''
        data = request.data
        posttag = Post.objects.get(id=data['id'])
        data['amount'] = posttag.reward
        data['pay_user'] = posttag.author.id
        data['title'] = posttag.title
        data['status'] = 100
        data['post'] = posttag.id
        data['receive_user'] = data['userid']
        serializer = OrderSerializer(data=data)
        if serializer.is_valid():
            try:
                order = serializer.save()
                posttag.status=300
                posttag.save()
            except:
                return Response(data={'error_msg': serializer.errors}, status=400)
            return Response(data={'msg': 'success'}, status=200)
        return Response(data={'error_msg': serializer.errors}, status=400)

class CancelPostAPI(APIView):
    '''
    取消需求.
    '''
    permission_classes = (IsAuthenticated,)
    @classmethod
    def post(cls, request):
        '''
        通过需求贴ID定位需求帖.
        '''
        data = request.data
        posttag = Post.objects.get(id=data['id'])
        try:
            Order.objects.filter(post=posttag).update(status=500)
        except:
            return Response(data={'error_msg': 'Unsuccess'}, status=400)
        posttag.status=500
        posttag.save()
        return Response(data={'msg': 'success'}, status=200)

class CloseOrderByDevAPI(APIView):
    '''
    开发者放弃开发, 关闭订单.
    '''
    permission_classes = (IsAuthenticated,)
    @classmethod
    def post(cls, request):
        '''
        通过需求贴ID定位需求帖.
        '''
        data = request.data
        posttag = Post.objects.get(id=data['id'])
        try:
            Order.objects.filter(post=posttag).filter(receive_user=GetUser(data['userid'])).update(status=200)
        except:
            return Response(data={'error_msg': 'Unsuccess'}, status=400)
        posttag.status=200
        posttag.save()
        return Response(data={'msg': 'success'}, status=200)


class CloseOrderByUserAPI(APIView):
    '''
    发起需求用户关闭订单.
    '''
    permission_classes = (IsAuthenticated,)
    @classmethod
    def post(cls, request):
        '''
        通过需求贴ID定位需求帖.
        '''
        data = request.data
        posttag = Post.objects.get(id=data['id'])
        try:
            Order.objects.filter(post=posttag).filter(pay_user=GetUser(data['userid'])).update(status=200)
        except:
            return Response(data={'error_msg': 'Unsuccess'}, status=400)
        posttag.status=200
        posttag.save()
        return Response(data={'msg': 'success'}, status=200)


class FinishOrderAPI(APIView):
    '''
    由需求发起用户完成订单.
    '''
    permission_classes = (IsAuthenticated,)
    @classmethod
    def post(cls, request):
        '''
        通过需求贴ID定位需求帖.
        '''
        data = request.data
        posttag = Post.objects.get(id=data['id'])
        try:
            Order.objects.filter(post=posttag).filter(pay_user=GetUser(data['userid'])).update(status=300)
        except:
            return Response(data={'error_msg': 'Unsuccess'}, status=400)
        posttag.status=400
        posttag.save()
        return Response(data={'msg': 'success'}, status=200)
