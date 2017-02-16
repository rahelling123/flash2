from django.conf.urls import url
from django.contrib import admin
from video.views import index, UploadVideo, VideoView, upload, create_rating, video_ratings

urlpatterns = [
    url(r'^upload', UploadVideo.as_view(), name='upload'),
    url(r'^(?P<pk>[0-9]+)/$', VideoView.as_view(), name='videoview'),
    # url(r'^ratings', RatingView.as_view(success_url='success_yea'), name='ratingview'),
    url(r'^success', upload, name='success_yea'),
    url(r'^(?P<video_id>\d+)/create_rating', create_rating, name='create_rating'),
    # url(r'^(?P<video_id>\d+)/ratings', RatingView.as_view(success_url='success_yea'), name='rating_view'),
    url(r'^(?P<video_id>\d+)/success', upload, name='success_yea'),
    url(r'^ratings', video_ratings, name='video_ratings')

]