from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
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


def add(request):
  template = loader.get_template('add.html')
  context = {
  
  }
  return HttpResponse(template.render(context, request))




def addrecord(request):
  x = request.POST['first']
  y = request.POST['last']
  member = Sheets(firstname=x, lastname=y)
  member.save()
  return HttpResponseRedirect(reverse('slicy'))
  

def delete(request ,id):
  member = Sheets.objects.get(id=id)
  member.delete()
  return HttpResponseRedirect(reverse('slicy'))


def update(request, id):
  mymember = Sheets.objects.get(id=id)
  template = loader.get_template('update.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))


def updaterecord(request, id):
  first = request.POST['first']
  last = request.POST['last']
  member = Sheets.objects.get(id=id)
  member.firstname = first
  member.lastname = last
  member.save()
  return HttpResponseRedirect(reverse('slicy'))