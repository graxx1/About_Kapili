from turtle import home
from django.urls import path
from myapp.views import *
from django.contrib.auth import views as auth_views

urlpatterns = [

path('', Home.as_view(), name='home'),
path('aboutme/', AboutMe.as_view(), name='login'),
]