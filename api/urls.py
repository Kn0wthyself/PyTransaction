"""py_transaction URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token

from api import views
from api.views import post

urlpatterns = [
    url('helloworld$', views.HelloWorldAPI.as_view()),
    url('v1/login$', views.LoginView.as_view()),
    url('v1/register$', views.RegisterAPI.as_view()),
    url('v1/basic-info$', views.BasicInfoAPI.as_view()),
    url('v1/modify-password$', views.ModifyPasswordAPI.as_view()),
    url('v1/verify-token$', verify_jwt_token),
    url('v1/create-posttag$', views.post.CreatePostAPI.as_view()),
    url('v1/accept-post$', views.post.AcceptPostAPI.as_view()),
    url('v1/cancel-post$', views.post.CancelPostAPI.as_view()),
    url('v1/close-post-dev$', views.post.CloseOrderByDevAPI.as_view()),
    url('v1/close-post-user$', views.post.CloseOrderByUserAPI.as_view()),
    url('v1/finish-post$', views.post.FinishOrderAPI.as_view()),
    url('v1/get-my-orders$', views.post.GetMyOrdersAPI.as_view()),
    url('v1/get-orders/(?P<user_id>.+)$', views.post.GetOnesOrdersAPI.as_view()),
    url('v1/get-all-orders$', views.post.GetAllOrdersAPI.as_view()),
    url('v1/get-order-by-id/(?P<post_id>.+)$', views.post.GetOrderByIdAPI.as_view()),
]
