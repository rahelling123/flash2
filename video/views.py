from django.http import HttpResponse, request
from django.shortcuts import render, get_object_or_404
from django.template import loader

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import DetailView

from video.models import Video, Rating


def index(request):
    template = loader.get_template('index.html')
    vidall = Video.objects.order_by('-date_created')[:5]
    context = {
        'vidall': vidall
    }
    return HttpResponse(template.render(context, request))


class UploadVideo(CreateView):
    model = Video
    fields = ['title', 'description']
    template_name = 'upload_video.html'
    success_url = reverse_lazy('index')


class VideoView(DetailView):
    model = Video
    template_name = 'video_view.html'


def create_rating(request, video_id):
    vid = get_object_or_404(Video, pk=video_id)
    past_ratings = Rating.objects.filter(pk=video_id)
    template = loader.get_template('create_rating.html')
    context = {
        'vid': vid, 'past_rating': past_ratings
    }
    return HttpResponse(template.render(context, request))


def upload(request, video_id):
    template = loader.get_template('rating_uploaded.html')
    video1 = Video.objects.get(id(video_id))
    context = {'video1': video1}
    return HttpResponse(template.render(request, context))


def video_ratings(request):
    template = loader.get_template('ratings.html')
    p_ratings = Rating.objects.all()
    vid_rate = Video.objects.get(pk=1)
    ratings_of_video = vid_rate.rating.all()
    context = {
        'p_ratings': p_ratings, 'vid_rate': vid_rate, 'ratings_of_video': ratings_of_video
    }
    return HttpResponse(template.render(context, request))
