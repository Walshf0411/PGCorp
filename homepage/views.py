from django.http import HttpResponse
from django.views import generic
from .models import Flat
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy


def index(request):
    return HttpResponse('<h1>This is the landing page</h1>')


class FlatView(generic.ListView):
    model = 'Flat'
    template_name = 'homepage/flatlist.html'
    context_object_name = 'flats'

    def get_queryset(self):
        return Flat.objects.all()


class DetailView(generic.DetailView):
    model = 'Flat'
    template_name = 'homepage/detail.html'
    context_object_name = 'flat'


class FlatCreate(CreateView):
    model = 'Flat'
    fields = ['nearest_railway_station', 'number_of_members', 'preferred_guests', 'price',
              'price_negotiable', 'description']


class FlatUpdate(UpdateView):
    model = 'Flat'
    fields = ['nearest_railway_station', 'number_of_members', 'preferred_guests', 'price', 'price_negotiable', 'description']


class FlatDelete(DeleteView):
    model = 'Flat'
    success_url = reverse_lazy('homepage:flats')

