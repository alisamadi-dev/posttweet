from django.db import models

# Create your models here.


class Tweet (models.Model):
    tweetTitle = models.TextField()

    def __str__(self):
        return self.tweetTitle
