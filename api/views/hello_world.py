# -*- coding: utf8 -*-
from rest_framework.views import APIView
from rest_framework.response import Response


class HelloWorldAPI(APIView):

    @classmethod
    def get(cls, request):
        return Response({'data': 'hello world'})
