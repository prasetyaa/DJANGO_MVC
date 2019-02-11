from django.db import models

from django.db.models import TextField
from django.db.models import CharField
from django.db.models import DateTimeField
from django.utils import timezone
# Create your models here.

class Direksi(models.Model):
    nama_lengkap = models.CharField(max_length=255)
    no_telepon = models.TextField(max_length=30)
    jabatan = models.CharField(max_length=255)

class Mentee(models.Model):
    nama_lengkap = models.CharField(max_length=255)
    no_telepon = models.TextField(max_length=30)
    nomor_absen = models.TextField(max_length=100)
    nilai_rata_rata = models.TextField(max_length=255)

class MataPelajaran(models.Model):
    nama_pelajaran = models.CharField(max_length=255)
    jadwal_dimulai = models.DateTimeField(default=timezone.now)
    jadwal_berakhir = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nama_pelajaran

class Mentor(models.Model):
    nama_lengkap = models.CharField(max_length=255)
    no_telepon = models.TextField(max_length=30)
    mata_pelajaran = models.ForeignKey(MataPelajaran, on_delete= models.CASCADE)

class Challenge(models.Model):
    nama_challenge = models.CharField(max_length=255)
    banyak_soal = models.TextField(max_length=100)
    bobot_nilai = models.TextField(max_length=255)
    mata_pelajaran = models.ForeignKey(MataPelajaran, on_delete= models.CASCADE)

class LiveCode(models.Model):
    nama_live_code = models.CharField(max_length=255)
    banyak_soal = models.TextField(max_length=100)
    bobot_nilai = models.TextField(max_length=255)
    tanggal_pelaksanaan = models.DateTimeField(default=timezone.now)
    mata_pelajaran = models.ForeignKey(MataPelajaran, on_delete= models.CASCADE)
    