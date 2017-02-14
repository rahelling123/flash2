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
    success_url = '/success_yea/'

    def get_initial(self):
        return dict(video=Video.objects.get(id=self.kwargs['video_id']))


def create_rating(request, video_id):
    vid = get_object_or_404(Video, pk=video_id)
    video_list = Video.objects.order_by('-date_created')[:5]
    template = loader.get_template('create_rating.html')
    context = {
        'vid': vid, 'video_list': video_list, 'range': range(8)
    }
    return HttpResponse(template.render(context, request))


def upload(request, video_id):
    template = loader.get_template('rating_uploaded.html')
    video1 = Video.objects.get(id(video_id))
    context = {'video1': video1}
    return HttpResponse(template.render(request, context))
