from django import forms
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

from pendampingan.models import MataKuliah


class MataKuliahCreateUpdateForm(forms.ModelForm):    
    class Meta:        
        model = MataKuliah
        fields = ['kode', 'nama', 'jumlah_sks', 'semester', 'deskripsi', 'uniid_pengampu',]

        labels = {
            'kode': 'Kode Mata Kuliah',
            'is_active': 'Aktifkan Kurikulum'
        }

        widgets = {
            'kode': forms.TextInput(attrs={'placeholder': 'Misal: CH00123'}),            
            'nama': forms.TextInput(attrs={'placeholder': 'Misal: Kesehatan Anak'}),
            'jumlah_sks': forms.TextInput(attrs={'type': 'number', 'placeholder': 'Misal: 2'}),
            'semester': forms.TextInput(attrs={'type': 'number', 'placeholder': 'Misal: 1'}),
            'deskripsi': forms.TextInput(attrs={'placeholder': 'Misal: Kesehatan anak pada usia dini...'}),
            'uniid_pengampu': forms.TextInput(attrs={'placeholder': 'Misal: tr122'}),
        }        
        
