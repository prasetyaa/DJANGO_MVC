from django.db import models
from django.db.models import TextField
from django.db.models import CharField
# Create your models here.

class Dokter(models.Model):
    nama = models.CharField(max_length=255)
    nomor_telepon = models.TextField(max_length=25)
    bidang = models.TextField(max_length=255)
    jadwal_praktek = models.CharField(max_length=255)

class Pasien(models.Model):
    nama = models.CharField(max_length=255)
    nomor_telepon = models.TextField(max_length=25)
    alamat = models.TextField(max_length=255)
    keluhan = models.CharField(max_length=255)

class Resep(models.Model):
    nama = models.CharField(max_length=255)
    total_harga = models.TextField(max_length=100)
    kumpulan_obat = models.CharField(max_length=255)

class Obat(models.Model):
    nama = models.CharField(max_length=255)
    kandungan = models.CharField(max_length=255)
    khasiat = models.CharField(max_length=255)
