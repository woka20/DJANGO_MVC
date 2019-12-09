from django.db import models

# Create your models here.

class Dokter(models.Model):
    nama=models.CharField(max_length=200)
    no_telepon=models.CharField(max_length=30)
    bidang=models.CharField(max_length=300)
    jadwal_praktek=models.DateTimeField('Jadwal Praktek')

    def __str__(self):
        return self.nama


class Pasien(models.Model):
    nama=models.CharField(max_length=200)
    no_telepon=models.CharField(max_length=30)
    alamat=models.CharField(max_length=300)
    keluhan=models.CharField(max_length=200)

    def __str__(self):
        return self.nama


class Obat(models.Model):
    nama_obat=models.CharField(max_length=300)
    kandungan=models.CharField(max_length=200)
    khasiat= models.CharField(max_length=500) 

    def __str__(self):
        return self.nama_obat

class Resep(models.Model):
    nama_pasien=models.CharField(max_length=200)
    total_harga=models.DecimalField(max_digits=10, decimal_places=3)
    kumpulan_obat=models.ForeignKey(Obat, on_delete=models.CASCADE)

    def __str__(self):
        return self.nama_pasien
    

