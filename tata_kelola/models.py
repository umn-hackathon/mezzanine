from django.db import models
from django.contrib.auth.models import User


KATEGORI_APLIKASI = (
    ('PP', 'Pelayanan Publik'),
    ('MI', 'Manajemen Internal')
)

MEKANISME_PENGANGGARAN= (
    ('O', 'Pengeluaran Operasi'),
    ('C', 'Pengeluaran Modal')
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

class Step2(models.Model):
    proyek = models.ForeignKey(Proyek)
    mekanisme_penganggaran = models.CharField(max_length=32, choices=MEKANISME_PENGANGGARAN)
    umur_ekonomis = models.IntegerField(help_text='dalam bulan')
    ketersediaan_anggaran = models.FileField()
    tingkat_kecepatan_keusangan = models.TextField()
    nilai_startegis_tik = models.TextField()
    karakteristik_proyek = models.TextField()
    urgensi = models.TextField()
    ketersediaan_pemasok = models.TextField()
    ketersediaan_sumber_daya = models.TextField()
    capital_budgeting = models.TextField()
    visi = models.TextField()
    misi = models.TextField()