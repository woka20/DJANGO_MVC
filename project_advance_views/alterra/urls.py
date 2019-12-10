from django.urls import path
from . import views


urlpatterns=[
    path('',  views.home, name="home"),
    path('blog/',  views.blog, name="blog"),
    path('mentee/',  views.mentee, name="mentee"),
    path('mentor/',  views.mentor, name="mentor"),
    path('about/', views.author, name="about"),
    path('submit-form/', views.form, name="submit"),
    path('submit', views.submit, name="todb")

]