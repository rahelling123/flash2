from django.contrib.auth import login
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.template import loader
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.views import login

from video.views import index

# Create your views here.



def user_account(request):
    template = loader.get_template("user_management/profile.html")
    if request.user.is_authenticated:
        username = request.user.username
        context = {
            'username': username
        }
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect(reverse(login))
    return HttpResponse(template.render(request))

