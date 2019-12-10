from django.shortcuts import render, redirect
from .models import Blog, Mentor, Mentee

# Create your views here.


def home(request):
    return render(request, 'alterra/index.html')

def blog(request):
    blogs=Blog.objects.all()
    return render(request, 'alterra/blog.html', {'blogs':blogs})

def mentor(request):
    mentors_data=Mentor.objects.all()
    return render(request, 'alterra/mentor.html', {'mentors': mentors_data})

def mentee(request):
    mentees=Mentee.objects.all()
    return render(request, 'alterra/mentee.html', {'mentees': mentees})

def author(request):
    return render(request, 'alterra/author.html')

def form(request):
    return render(request, 'alterra/input-blog.html')


def submit(request):
    Posting=Blog(
        judul=request.POST['judul_post'],
        konten=request.POST['konten_post'],
        gambar=request.POST['gambar_post']

    )
    Posting.save()
    return redirect('blog/')
    

