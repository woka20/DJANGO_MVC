from django.db import models

# Create your models here.

class Direksi(models.Model):
    nama=models.CharField(max_length=200)
    no_telepon=models.CharField(max_length=30)
    jabatan=models.CharField(max_length=300)
    
    def __str__(self):
        return self.nama
    


class Mentee(models.Model):
    nama=models.CharField(max_length=200)
    no_telepon=models.CharField(max_length=30)
    nomor=models.IntegerField(max_length=5)
    nilai_rata=models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nama

class MataPelajaran(models.Model):
    nama_pelajaran=models.CharField(max_length=200)
    jadwal_mulai=models.CharField(max_length=30)
    jadwal_akhir=models.CharField(max_length=30)

    def __str__(self):
        return self.nama_pelajaran


class Mentor(models.Model):
    nama=models.CharField(max_length=200)
    no_telepon=models.CharField(max_length=30)
    mata_pelajaran=models.ForeignKey(MataPelajaran, on_delete=models.CASCADE)

    def __str__(self):
        return self.nama
    
class Challenge(models.Model):
    nama_challenge=models.CharField(max_length=200)
    banyak_soal= models.IntegerField(max_length=5)
    bobot_nilai= models.DecimalField(max_digits=10, decimal_places=2)
    mata_pelajaran= models.ForeignKey(MataPelajaran, on_delete=models.CASCADE)

    def __str__(self):
        return self.nama_challenge

class LiveCode(models.Model):
    nama_live_code=models.CharField(max_length=200)
    banyak_soal=models.IntegerField(max_length=5)
    bobot_nilai= models.DecimalField(max_digits=10, decimal_places=2)
    tanggal_pelaksanaan= models.DateTimeField("Jadwal_Ujian")
    mata_pelajaran= models.ForeignKey(MataPelajaran, on_delete=models.CASCADE)

    def __str__(self):
        return self.nama_live_code
