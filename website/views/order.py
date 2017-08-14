from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class post_order(TemplateView):
    template_name = 'post_order.html'

class order_list(TemplateView):
    template_name = 'order_list.html'

class order_dev_list(TemplateView):
    template_name = 'order_dev_list.html'

class all_orders(TemplateView):
    template_name = 'all_orders.html'

class order_detail(TemplateView):
    template_name = 'order_detail.html'