from django.conf.urls import url
from django.contrib import admin
from video.views import index, UploadVideo, VideoView, create_rating, rating_upload

urlpatterns = [
    url(r'^upload', UploadVideo.as_view(), name='upload'),
    url(r'^(?P<pk>[0-9]+)/$', VideoView.as_view(), name='videoview'),
    url(r'^(?P<video_id>\d+)/create_rating', create_rating, name='create_rating'),
    url(r'^(?P<video_id>\d+)/rating_upload', rating_upload, name='rating_upload'),
    url(r'^(?P<video_id>\d+)/rating_uploaded', rating_upload, name='rating_upload')
]
