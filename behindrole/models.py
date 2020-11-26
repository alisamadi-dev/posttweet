from django.db import models
from django.urls import reverse

# Create your models here.


class Tweet (models.Model):
    tweetTitle = models.CharField(max_length=150)
    #author = models.ForeignKey('auth.user', on_delete=models.CASCADE,)
    body = models.TextField()

    def __str__(self):
        return self.tweetTitle

    def get_absolute_url(self):
        return reverse('tweet_detail', args=[(self.id)])
