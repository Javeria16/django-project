from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Sheets

def index(request):
    return HttpResponse("Hello world!")

def indexhtml(request):
  template = loader.get_template('myfirst.html')
  x=5+5+5
  context = {
    'varname': x,
    'binaryofx': bin(x)[2::]
  }
  return HttpResponse(template.render(context, request))
  
def myfile(request):
  template = loader.get_template('abc.html')
  mymembers = Sheets.objects.all().values()
  context = {
    'jam':mymembers,
  }
  return HttpResponse(template.render(context, request))


def slicy(request):
  mymem = Sheets.objects.all().values()
  template = loader.get_template('javi.html')
  context = {
    'var': mymem,
  }
  return HttpResponse(template.render(context, request))
