from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.utils.translation import gettext_lazy as _


class SigninForm(forms.Form):
    username    = forms.CharField(required=True)
    password    = forms.CharField(required=True)

    # class Meta:        
    #     fields = ['username', 'password']
        
