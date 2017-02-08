from django import forms
from django.forms import ModelForm
from video.models import Video


class RatingForm(ModelForm):
    class Meta:
        model = Video
        fields = ['comment', 'rating']