from django.db import models
from django.contrib.auth.models import User


KATEGORI_APLIKASI = (
    ('PP', 'Pelayanan Publik'),
    ('MI', 'Manajemen Internal')
)

class Proyek(models.Model):
    nama_proyek = models.CharField(max_length = 128)
    latest_step = models.CharField(max_length=32)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    opd = models.ForeignKey(User)


class Step1(models.Model):
    proyek = models.ForeignKey(Proyek)
    arsitektur_informasi = models.FileField()
    kategori_aplikasi = models.CharField(max_length=32, choices=KATEGORI_APLIKASI)
    infrastruktur_komunkasi = models.FileField()
    infrastruktur_penyimpanan_data = models.FileField()
    organisasi_manajemen_realisasi = models.FileField()
    organisasi_manajemen_operasi = models.FileField()
    organisasi_manajemen_pemeliharaan = models.FileField()
    estimasi_waktu = models.IntegerField(help_text='dalam bulan')