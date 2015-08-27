from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<app_id>[0-9]+)/$', views.app, name='app'),
    url(r'^servers/$', views.servers, name='servers'),
    url(r'^servers/(?P<server_id>[0-9]+)/$', views.server, name='server'),
    url(r'^services/$', views.services, name='services'),
    url(r'^services/(?P<service_id>[0-9]+)/$', views.service, name='service'),
    url(r'^skills/$', views.skills, name='skills'),
]