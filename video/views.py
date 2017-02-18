from audioop import reverse

from django.http import HttpResponse, request
from django.http import HttpResponseRedirect
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
    past_ratings = vid.rating.order_by('date_created')[:5]
    template = loader.get_template('create_rating.html')
    context = {
        'vid': vid, 'past_ratings': past_ratings
    }
    return HttpResponse(template.render(context, request))


def rating_upload(request, video_id):
    template = loader.get_template('rating_upload.html')
    rated_video = Video.objects.get(pk=video_id)
    context = {
        'rated_video': rated_video
    }
    return HttpResponse(template.render(context, request))
