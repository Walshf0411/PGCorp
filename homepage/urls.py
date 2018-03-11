from django.conf.urls import url
from . import views
from .models import Flat

app_name = 'homepage'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^flats/$', views.FlatView.as_view(), name='flats'),
    url(r'^flats/(?P<pk>[0-9]+)/$', views.DetailView.as_view(model=Flat), name='detail'),
    url(r'^flats/post/$', views.FlatCreate.as_view(model=Flat), name='flat-create'),
    url(r'^flats/update/(?P<pk>[0-9]+)/$', views.UpdateView.as_view(model=Flat), name='flat-update'),
    url(r'^flats/(?P<pk>[0-9]+)/delete', views.FlatDelete.as_view(model=Flat), name='flat-delete'),
    url(r'^membership/$', views.membership, name='membership'),
    url(r'^services/$', views.services, name='services')
]
