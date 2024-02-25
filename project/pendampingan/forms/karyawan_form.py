from django import forms
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

from pendampingan.models import Karyawan


class KaryawanCreateUpdateForm(forms.ModelForm):    
    class Meta:        
        model = Karyawan
        fields = ['user', 'is_active', 'namalengkap', 'namabergelar', 'homebase_uniid']
        
