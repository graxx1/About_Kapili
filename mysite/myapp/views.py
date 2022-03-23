from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from .models import Me
from django.contrib.auth.models import User


# Create your views here.

class Home(View):
    def get(self, request):
        return render(request, 'Home.html')

class Me(View):
    def get(self, request):
        return render(request, 'AboutMe.html')