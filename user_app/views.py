import datetime
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template import loader
from django.template import RequestContext

# Create your views here.
from django.urls import reverse
from django.views.decorators.csrf import csrf_protect


def signup_page(request):
    return render(request, "user_app/signup_page.html")


def signup(request):
    template = loader.get_template('user_app/profile.html')
    if request.method == "POST":

        username = request.POST['username']
        password = request.POST['password']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        kwargs = {
            'username': username, 'password': password, 'first_name': first_name,
            'last_name': last_name, 'email': email
        }
        new_user = User.objects.create(**kwargs)
        new_user.save()
        context = {
            'first_name': first_name, 'last_name': last_name, 'username': username
        }
        user_id = new_user.pk
        return HttpResponseRedirect(reverse('profile', args=(user_id,)))
    else:
        return HttpResponse(template.render(request))


def profile(request, user_id):
    logged_in_user = User.objects.get(pk=user_id)
    context = {
        'logged_in_user': logged_in_user
    }
    template = loader.get_template('user_app/profile.html')
    return HttpResponse(template.render(context, request))
