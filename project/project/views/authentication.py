from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.models import User

from project.forms.authentication_form import SigninForm
from services.decorators import isloggedin


# =====================================================================================================
#                                               LOAD PAGE
# =====================================================================================================
@isloggedin('dashboard')
def signin(request):
    context = {}
    context['formsignin'] = SigninForm(request.POST or None)

    if request.POST:
        if context['formsignin'].is_valid():
            username = context['formsignin'].cleaned_data.get('username')
            password = context['formsignin'].cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:                
                login(request, user)
                messages.success(request, 'Login berhasil')

                next = request.GET.get('next', 'dashboard')
                return redirect(next)                                    
            else:
                messages.warning(request, 'Mohon cek kembali username dan password anda')                
        else:            
            messages.error(request, context['formsignin'].errors)
            # messages.error(request, context['formsignin'].errors.get_json_data()['__all__'][0]['message'])
    

    return render(request, 'authentication/signin.html', context)




def signout(request):
    logout(request)
    
    storage = messages.get_messages(request)
    if storage:
        for message in storage:
            messages.warning(request, message)
    else:
        messages.success(request, 'Anda berhasil logout')

    return redirect('signin')
