import datetime
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.template import RequestContext


# Create your views here.

def signup_page(request):
    template = loader.get_template('user_app/signup_page.html')
    template_profile = loader.get_template('user_app/profile.html')

    if request.method == "POST":

        username = request.POST['username']
        password = request.POST['password']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        kwargs = {
            'username':username, 'password':password, 'first_name':first_name,
            'last_name':last_name, 'email':email
        }
        new_user = User.objects.create(**kwargs)
        new_user.save()

        context = {
            'text':"POST", 'first_name':first_name
        }

        return HttpResponse(template_profile.render(RequestContext(request), context))
    else:
        return HttpResponse(template.render(request))


def profile(request):
    return HttpResponse(RequestContext(request))