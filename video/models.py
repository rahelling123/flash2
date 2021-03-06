from __future__ import unicode_literals

import datetime

from django.db import models


# Create your models here.
class Video(models.Model):
    CHOICES = ((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'))
    date_created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, default="Community Video   ")
    description = models.CharField(max_length=200)
    flash_video = models.FileField(verbose_name='flash_video')
    rating_int = models.IntegerField(default=1, choices=CHOICES, name='rating_int')
    comment = models.TextField(max_length=500, default="this is great")

    def __str__(self):
        return self.title


class Rating(models.Model):
    rate_choice = ((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'))
    rate_value = models.IntegerField(default=5, choices=rate_choice)
    video = models.ForeignKey('Video', related_name='rating', null=True)
    rate_comment = models.CharField(max_length=200, default="No Comment")
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.rate_comment
