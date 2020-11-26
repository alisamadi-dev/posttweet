from .models import Tweet
from django.views.generic import ListView, DetailView
from django.shortcuts import render
# from django.http import HttpResponse
# Create your views here.
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView
# def homepage_view(request):
# return HttpResponse("i am here !")

# class HomePageView(TemplateView):
#     template_name = 'home.html'


class HomePageView(ListView):
    model = Tweet
    template_name = 'home.html'
    context_object_name = 'all_tweets'


class AboutPageView(TemplateView):
    template_name = 'about.html'


class TweetPageView(DetailView):
    model = Tweet
    template_name = 'tweet.html'
    context_object_name = 'tweet_obj'


class TweetCreateView(CreateView):
    model = Tweet
    template_name = 'tweet_new.html'
    fields = ['tweetTitle', 'body']
