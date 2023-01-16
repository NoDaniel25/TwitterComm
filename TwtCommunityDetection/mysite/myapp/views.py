# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.template import context

from .source.visualisationUtils import *

def index(request):
    return HttpResponse("Hello world")

def girvanNewman(request):
    context['graph'] = return_graph()
    return render(request, 'base.html', context)

def getimage(request):
    context['graph'] = return_graph()
    return render(request, 'base.html', context)