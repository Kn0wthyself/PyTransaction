from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


class admin(TemplateView):
    template_name = 'admin.html'

class profile(TemplateView):
    template_name = 'profile.html'    

class login(TemplateView):
    template_name = 'login.html'    

class join(TemplateView):
    template_name = 'join.html'
