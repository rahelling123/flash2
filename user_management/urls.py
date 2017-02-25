from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from user_management.views import user_account

urlpatterns =[
    url(r'^login', auth_views.login, {'template_name':'user_management/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^admin', admin.site.urls),
    url(r'^account', user_account, name='user_account'),
    url(r'^logout', auth_views.logout, {'template_name':''}, name='logout'),

]
