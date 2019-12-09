from django.db import models

# Create your models here.

class Hewan(models.Model):
    nama=models.CharField(max_length=200)
    spesies=models.CharField(max_length=30)
    berat=models.IntegerField(max_length=300)
    umur=models.IntegerField(max_length=10)

    def __str__(self):
        return self.nama

class Kandang(models.Model):
    nama=models.CharField(max_length=200)
    isi_kandang=models.CharField(max_length=30)
    luas=models.IntegerField(max_length=10)

    def __str__(self):
        return self.nama

class Penjaga(models.Model):
    nama=models.CharField(max_length=200)
    telepon=models.CharField(max_length=30)
    jadwal_jaga=models.DateTimeField('Jadwal Jaga')

    def __str__(self):
        return self.nama

class Pengunjung(models.Model):
    nama=models.CharField(max_length=200)
    telepon=models.CharField(max_length=30)
    jadwal_jaga=models.DateField('Hari Berkunjung')

    def __str__(self):
        return self.nama
