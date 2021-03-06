# Generated by Django 2.1.5 on 2019-02-11 09:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Challenge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_challenge', models.CharField(max_length=255)),
                ('banyak_soal', models.TextField(max_length=100)),
                ('bobot_nilai', models.TextField(max_length=255)),
                ('mata_pelajaran', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Direksi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_lengkap', models.CharField(max_length=255)),
                ('no_telepon', models.TextField(max_length=30)),
                ('jabatan', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='LiveCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_live_code', models.CharField(max_length=255)),
                ('banyak_soal', models.TextField(max_length=100)),
                ('bobot_nilai', models.TextField(max_length=255)),
                ('tanggal_pelaksanaan', models.DateTimeField(default=django.utils.timezone.now)),
                ('mata_pelajaran', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='MataPelajaran',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_pelajaran', models.CharField(max_length=255)),
                ('jadwal_dimulai', models.DateTimeField(default=django.utils.timezone.now)),
                ('jadwal_berakhir', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Mentee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_lengkap', models.CharField(max_length=255)),
                ('no_telepon', models.TextField(max_length=30)),
                ('nomor_absen', models.TextField(max_length=100)),
                ('nilai_rata_rata', models.TextField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_lengkap', models.CharField(max_length=255)),
                ('no_telepon', models.TextField(max_length=30)),
                ('mata_pelajaran', models.CharField(max_length=255)),
            ],
        ),
    ]
