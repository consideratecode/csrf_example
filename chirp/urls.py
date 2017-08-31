from django.conf.urls import url

from . import views

app_name = 'chirp'
urlpatterns = [
    url(r'^$', views.create_user, name='create_user'),
    url(r'^status/$', views.create_status, name='create_status'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^(?P<username>[a-zA-Z0-9]*)/$', views.profile, name='profile'),
]
