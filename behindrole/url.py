

from django.urls import path
from .views import HomePageView, TweetPageView, AboutPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('tweet/<int:pk>/', TweetPageView.as_view(), name='tweet_detail'),

]
