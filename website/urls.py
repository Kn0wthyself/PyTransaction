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

from website import views

urlpatterns = [
    url('index', views.index.as_view()),
    url('login', views.login.as_view()),
    url('user_admin', views.admin.as_view()),
    url('join', views.join.as_view()),
    url('profile', views.profile.as_view()),
    url('about', views.about.as_view()),
    url('order_list', views.order_list.as_view()),
    url('post_order', views.post_order.as_view()),
    url('all_orders', views.all_orders.as_view()),
    url('order_detail/(?P<order_id>[0-9]+)', views.order_detail.as_view()),
    url(r'^$', views.index.as_view()),
]
