from rest_framework_jwt.views import JSONWebTokenAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from api.serializer.auth import JSONWebTokenSerializer, UserSerializer

class BasicInfoAPI(APIView):
    # update BacisInformation
    permission_classes = (IsAuthenticated,)
    @classmethod
    def get(cls, request):
        user = request.user
        return Response({'nickname': user.username, 'email': user.email})

# class ModifyBasicInfoAPI(APIView):
#     # update BacisInformation
#     permission_classes = (IsAuthenticated,)
#     @classmethod
#     def post(cls, request):
#         data = request.data
#         if 'old_password' not in data or 'new_password' not in data:
#             return Response({'error_msg': '参数错误'}, status=400)
#         user = request.user
#         if user.check_password(data['old_password']):
#             user.set_password(data['new_password'])
#             user.save()
#             return Response({'msg': '密码修改成功'})
#         return Response({'error_msg': '密码错误'}, status=400)
