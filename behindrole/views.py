from .models import Tweet
from django.views.generic import ListView
from django.shortcuts import render
# from django.http import HttpResponse
# Create your views here.
from django.views.generic import TemplateView

# def homepage_view(request):
# return HttpResponse("i am here !")

# class HomePageView(TemplateView):
#     template_name = 'home.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'


class HomePageView(ListView):
    model = Tweet
    template_name = 'home.html'
    context_object_name = 'all_tweets'
