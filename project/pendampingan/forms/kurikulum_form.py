from django import forms
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

from pendampingan.models import Kurikulum


class KurikulumCreateUpdateForm(forms.ModelForm):    
    class Meta:        
        model = Kurikulum
        fields = ['tahun', 'is_active']

        labels = {
            'is_active': 'Aktifkan Kurikulum'
        }

        widgets = {
            'tahun': forms.TextInput(attrs={'placeholder': 'Misal: 2022'}),            
        }        
        
