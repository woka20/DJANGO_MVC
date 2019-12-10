from django.db import models
from datetime import datetime


# Create your models here.

class Blog(models.Model):
    gambar=models.CharField(max_length=200)
    judul=models.CharField(max_length=80)
    tanggal=models.DateTimeField(default=datetime.now)
    konten=models.TextField(max_length=2500)
    komen=models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.judul

class Mentor(models.Model):
    gambar=models.CharField(max_length=200)
    nama=models.CharField(max_length=80)
    jabatan=models.CharField(max_length=100)
    qoute=models.CharField(max_length=80)

    def __str__(self):
        return self.nama

    

class Mentee(models.Model):
    gambar=models.CharField(max_length=200)
    nama=models.CharField(max_length=80)
    qoute=models.CharField(max_length=100)

    def __str__(self):
        return self.nama
    

