from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

from django.views.generic import TemplateView

# Create your views here.

def display(request):
	
	return HttpResponse('HELLO WORLD')
	
class HomePageView(TemplateView):
	template_name = 'home.html'

class AboutPageView(TemplateView):
	template_name = 'about.html'




