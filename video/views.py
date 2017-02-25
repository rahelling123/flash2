
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse, request
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.views.generic import CreateView
from django.views.generic import DetailView
from video.models import Video, Rating


# Create your views here.

def index(request):
    template = loader.get_template('index.html')
    vidall = Video.objects.order_by('-date_created')[:5]
    context = {
            'vidall': vidall
        }
    # if request.user.is_authenticated():
    #     username = request.user.username
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
    past_ratings = vid.rating.order_by('-date_created')[:5]
    template = loader.get_template('create_rating.html')
    context = {
        'vid': vid, 'past_ratings': past_ratings
    }
    return HttpResponse(template.render(context, request))


def rating_upload(request, video_id):
    rated_video = Video.objects.get(pk=video_id)

    try:
        rating_comment = request.POST.get('rate_comment')

    except (KeyError):
        return render(request, 'create_rating.html', video_id)

    else:
        new_rating = Rating(rate_comment=rating_comment, video=rated_video)
        new_rating.save()

    return HttpResponseRedirect(reverse('create_rating', kwargs={'video_id':video_id}))