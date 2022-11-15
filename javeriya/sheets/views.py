from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

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