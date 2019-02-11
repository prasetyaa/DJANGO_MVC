from django.db import models
from django.db.models import TextField
from django.db.models import CharField
# Create your models here.

class Hewan(models.Model):
    nama = models.CharField(max_length=255)
    species = models.CharField(max_length=100)
    berat = models.TextField(max_length=50)
    umur = models.CharField(max_length=100)

class Kandang(models.Model):
    nama = models.CharField(max_length=255)
    isi_kandang = models.CharField(max_length=255)
    luas_kandang = models.CharField(max_length=100)

class Penjaga(models.Model):
    nama = models.CharField(max_length=255)
    nomor_telepon = models.TextField(max_length=50)
    jadwal_jaga = models.CharField(max_length=255)

class Pengunjung(models.Model):
    nama = models.CharField(max_length=255)
    nomor_telepon = models.TextField(max_length=50)
    hari_berkunjung = models.CharField(max_length=255)