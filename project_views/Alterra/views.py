from django.shortcuts import render
from django.http import HttpResponse
# from .models import 

# Create your views here.

def home(request):
    return render(request, 'Alterra/index.html')

def blog(request):
    return render(request, 'Alterra/blog.html')

def mentor(request):
    return render(request, 'Alterra/mentor.html')

def mentee(request):
    return render(request, 'Alterra/mentee.html')

def author(request):
    return render(request, 'Alterra/author.html')
