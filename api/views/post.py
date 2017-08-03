from rest_framework.views import APIView
from rest_framework.response import Response

from api.serializer.auth import JSONWebTokenSerializer, UserSerializer
from api.serializer.post import OrderSerializer, PostTagSerializer
from api.models.user import EmployerProfile, DeveloperProfile
from api.models.post import PostTag
from api.models.transaction import Order

class CreatePostTagAPI(APIView):
    '''
    发表需求帖.
    '''

    @classmethod
    def post(cls, request):
        data = request.data
        # 使用当前登录用户作为发帖人.
        data['author'] = request.user
        serializer = PostTagSerializer(data=data)
        if serializer.is_valid():
            posttag = serializer.save()
            return Response(data={'msg': 'success'}, status=200)
        return Response(data={'error_msg': serializer.errors}, status=400)


class GetPostTagByIDAPI(APIView):
    '''
    通过ID获取需求帖.
    '''

    @classmethod
    def get(cls, request):
        data = request.data
        try:
            posttag = PostTag.objects.get(id=data['id'])
        except PostTag.DoesNotExist:
            return Response(data={'error_msg': 'DoesNotExist'}, status=404)
        return Response(data=PostTagSerializer(posttag), status=200)

class GetPostTagByAuthorAPI(APIView):
    '''
    获取某一用户发表的所有需求帖.
    '''

    @classmethod
    def get(cls, request):
        data = request.data
        user = EmployerProfile.objects.get(id=data['id'])
        # 按ID降序排列.
        posttag = PostTag.objects.filter(author=user).order_by('-id')
        return Response(data=PostTagSerializer(posttag, many=True), status=200)


class GetPostTagByDevAPI(APIView):
    '''
    获取某一用户接受的所有需求帖.
    '''

    @classmethod
    def get(cls, request):
        data = request.data
        user = DeveloperProfile.objects.get(id=data['id'])
        order = Order.objects.filter(receive_user=user)
        # 按ID降序排列.
        posttag = order.objects.post.order_by('-id')
        return Response(data=PostTagSerializer(posttag, many=True), status=200)


class GetPostTagAllAPI(APIView):
    '''
    获取已发表的所有需求帖.
    '''

    @classmethod
    def get(cls, request):
        # 按ID降序排列.
        posttag = PostTag.objects.all().order_by('-id')
        return Response(data=PostTagSerializer(posttag, many=True), status=200)


class AcceptPostAPI(APIView):
    '''
    接受订单.
    '''

    @classmethod
    def post(cls, request):
        '''
        通过需求贴ID定位需求帖.
        '''
        data = request.data
        posttag = PostTag.objects.get(id=data['id'])
        posttag.update(status=300)
        data['amount'] = posttag.reward
        data['pay_user'] = posttag.author
        data['title'] = posttag.title
        data['status'] = 100
        data['post'] = posttag
        serializer = OrderSerializer(data=data)
        if serializer.is_valid():
            order = serializer.save()
            return Response(data={'msg': 'success'}, status=200)
        return Response(data={'error_msg': serializer.errors}, status=400)

class CancelPostAPI(APIView):
    '''
    取消需求.
    '''

    @classmethod
    def post(cls, request):
        '''
        通过需求贴ID定位需求帖.
        '''
        data = request.data
        posttag = PostTag.objects.get(id=data['id'])
        posttag.update(status=500)
        try:
            Order.objects.filter(post=posttag).update(status=500)
        except:
            return Response(data={'error_msg': 'Unsuccess'}, status=400)
        return Response(data={'msg': 'success'}, status=200)

class CloseOrderByDevAPI(APIView):
    '''
    开发者放弃开发, 关闭订单.
    '''

    @classmethod
    def post(cls, request):
        '''
        通过需求贴ID定位需求帖.
        '''
        data = request.data
        posttag = PostTag.objects.get(id=data['id'])
        posttag.update(status=200)
        try:
            Order.objects.filter(post=posttag).filter(receive_user=request.user).update(status=200)
        except:
            return Response(data={'error_msg': 'Unsuccess'}, status=400)
        return Response(data={'msg': 'success'}, status=200)


class CloseOrderByUserAPI(APIView):
    '''
    发起需求用户关闭订单.
    '''

    @classmethod
    def post(cls, request):
        '''
        通过需求贴ID定位需求帖.
        '''
        data = request.data
        posttag = PostTag.objects.get(id=data['id'])
        posttag.update(status=200)
        try:
            Order.objects.filter(post=posttag).filter(pay_user=request.user).update(status=200)
        except:
            return Response(data={'error_msg': 'Unsuccess'}, status=400)
        return Response(data={'msg': 'success'}, status=200)


class FinishOrderAPI(APIView):
    '''
    由需求发起用户完成订单.
    '''

    @classmethod
    def post(cls, request):
        '''
        通过需求贴ID定位需求帖.
        '''
        data = request.data
        posttag = PostTag.objects.get(id=data['id'])
        posttag.update(status=400)
        try:
            Order.objects.filter(post=posttag).filter(pay_user=request.user).update(status=300)
        except:
            return Response(data={'error_msg': 'Unsuccess'}, status=400)
        return Response(data={'msg': 'success'}, status=200)
