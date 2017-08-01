from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class post_order(TemplateView):
    template_name = 'post_order.html'

class order_list(TemplateView):
    template_name = 'order_list.html'