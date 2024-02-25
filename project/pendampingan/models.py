from django.contrib.auth.models import User 
from django.db import models

# Create your models here.


class Lembaga(models.Model):
    uniid = models.CharField(max_length=255)
    nama = models.CharField(max_length=255)
    namasingkat = models.CharField(max_length=255, blank=True, null=True)
    superunit = models.CharField(max_length=255)
    namasuper = models.CharField(max_length=255)
    jenis_id = models.IntegerField(blank=True, null=True)
    jenis = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering    = ['id']

    def __str__(self):        
        return self.nama
    

class Karyawan(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)    
    is_active = models.BooleanField(default=True)
    namalengkap = models.CharField(max_length=255, blank=True, null=True)
    namabergelar = models.CharField(max_length=255, blank=True, null=True)
    homebase_uniid = models.CharField(max_length=255)
    namahomebase = models.CharField(max_length=255, blank=True, null=True)    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering    = ['id']

    def __str__(self):        
        return self.nama    