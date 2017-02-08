from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Video(models.Model):
    CHOICES = ((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'))
    date_created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, default="Community Video   ")
    description = models.CharField(max_length=200)
    flash_video = models.FileField(verbose_name='flash_video')
    rating = models.IntegerField(default=1, choices=CHOICES, name='rating')
    comment = models.TextField(max_length=500, default="this is great")

    def __str__(self):
        return self.title


class Rating(models.Model):
    rate_choice = ((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'))
    rate_value = models.IntegerField(default=5, choices=rate_choice)
    video = models.ForeignKey('Video', related_name='video', null=True, default=1)
