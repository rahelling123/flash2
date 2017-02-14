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


class RatingView(CreateView):
    model = Rating
    template_name = 'rating_create.html'
    fields = ['rate_value']


def upload(request):
    template = loader.get_template('rating_uploaded.html')
    return HttpResponse(template.render(request))


def create_rating(request):
    vid = get_object_or_404(Video, pk=1)
    video_list = Video.objects.all()
    template = loader.get_template('create_rating.html')
    context = {
        'vid': vid, 'video_list': video_list,
    }
    return HttpResponse(template.render(context, request))
