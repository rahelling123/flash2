from django.conf.urls import url
from user_app.views import signup_page, profile

urlpatterns = [
    url(r'^signup', signup_page, name="signup_page"),
    url(r'^profile', profile, name="profile")
]