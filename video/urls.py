from django.conf.urls import url
from django.contrib import admin
from video.views import index, UploadVideo, VideoView, RatingView, upload

urlpatterns = [
    url(r'^upload', UploadVideo.as_view(), name='upload'),
    url(r'^(?P<pk>[0-9]+)/$', VideoView.as_view(), name='videoview'),
    url(r'^ratings', RatingView.as_view(success_url='success_yea'), name='ratingview'),
    url(r'^success', upload, name='success_yea')
]
