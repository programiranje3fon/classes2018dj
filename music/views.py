# Create your views here.


from django.http import HttpResponse
from django.shortcuts import render

from music.models import Performer


def index(request):
    return HttpResponse('<h1>Hi there :)<h1>')


def performer_detail(request, pk):
    # return HttpResponse(str(Performer.objects.get(id=pk)))
    return HttpResponse(str(Performer.objects.get(id=pk).get_absolute_url()))


