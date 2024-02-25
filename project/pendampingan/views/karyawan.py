import json
from django.contrib.auth.models import User 
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import transaction
from django.db.models import Q

from django.http import JsonResponse


from django.urls import reverse
from json import dumps

from services.decorators import group_required

from pendampingan.models import Lembaga, Karyawan
from pendampingan.forms.karyawan_form import KaryawanCreateUpdateForm
from services.apigateway import apigateway


# =====================================================================================================
#                                               LOAD PAGE
# =====================================================================================================
@group_required('admin')
def table(request):
    context = {}

    # ===[Data]===
    datakaryawan = Karyawan.objects.all()
        
    # ===[context]===
    context['datakaryawan'] = datakaryawan
    context['sidebar'] = 'admin.karyawan'

    # ===[Render Template]===
    return render(request, 'adminpage/karyawan/table.html', context)


@group_required('admin')
@transaction.atomic
def sinkron(request):

    fakultas = Lembaga.objects.filter(Q(superunit="lmbg1015") | Q(uniid="lmbg1015"))    

    try:
        for lembaga in fakultas:
            apikaryawan = apigateway.get(f'umar/v3/karyawan?kepeg=dosen&homebase={lembaga.uniid}')            
            if apikaryawan['status']:
                for karyawan in apikaryawan['data']:
                    user, created = User.objects.update_or_create(username=karyawan['uniid'])                    
                    Karyawan.objects.update_or_create(
                        user=user,
                        defaults={
                            "namalengkap": karyawan['namalengkap'],
                            "namabergelar": karyawan['namabergelar'],
                            "homebase_uniid": karyawan['home_id'],
                            "namahomebase": karyawan['homebase'],                            
                        }
                    )                
            else:
                messages.error(request, apikaryawan)
                return redirect('pendampingan:admin_karyawan_table')
        messages.success(request, "Karyawan berhasil disinkronkan dengan SIHRD")
    except Exception as e:
        print(e)
        messages.error(request, str(e))

    return redirect('pendampingan:admin_karyawan_table')



# @group_required('admin')
# def add(request):
#     context = {}  

#     # ===[Load Form]===
#     context['karyawanform']     = KaryawanCreateUpdateForm(request.POST or None, request.FILES or None)

#     # ===[Insert Logic]===
#     if request.POST:
#         if context['karyawanform'].is_valid():
#             context['karyawanform'].save()
#             messages.success(request, 'Data Berhasil Ditambahkan')
#             return redirect('pendampingan:admin_karyawan_add')
#         else:
#             messages.error(request, context['karyawanform'].errors)

#     # ===[context]===
#     context['sidebar'] = 'admin.karyawan'            
    
#     # ===[Render Template]===
#     return render(request, 'adminpage/karyawan/add.html', context)


@group_required('admin')
def active_checked_json(request, id):
    try:
        karyawan = Karyawan.objects.get(id=id)                    
    except Karyawan.DoesNotExist:
        return JsonResponse({'status': False, 'message': f'Karyawan dengan id {id} tidak ditemukan'}, status=404)    
        
    json_data = json.loads(request.body)    
    karyawan.is_active = json_data['is_checked']
    karyawan.save()

    return JsonResponse({'status': True, 'message': f'Karyawan dengan id {id} berhasil diupdate'}, status=200)