from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('amresh/', views.indexhtml, name='indexhtml'),
    path('myfile/', views.myfile, name='myfile'),
    path('slicy/', views.slicy, name='slicy'),

]