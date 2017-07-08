from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


class profile(TemplateView):
    template_name = 'profile.html'