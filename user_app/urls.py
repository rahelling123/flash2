from django.conf.urls import url
from user_app.views import signup_page, profile, signup

urlpatterns = [
    url(r'^signup_page', signup_page, name="signup_page"),
    url(r'^profile/(?P<user_id>\d+)/', profile, name="profile"),
    url(r'^signup', signup, name="signup" )
]
