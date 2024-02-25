from django.shortcuts import render, get_object_or_404, reverse
from django.urls import path
from . import views as home_views

urlpatterns = [
    path('', home_views.home, name='home'),
    
]