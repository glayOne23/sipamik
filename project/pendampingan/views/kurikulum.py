import json
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User 
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import transaction
from django.db.models import Q

from django.http import JsonResponse


from django.urls import reverse
from json import dumps

from services.decorators import group_required

from pendampingan.models import Lembaga, Karyawan, Kurikulum
from pendampingan.forms.kurikulum_form import KurikulumCreateUpdateForm
from services.apigateway import apigateway


# =====================================================================================================
#                                               LOAD PAGE
# =====================================================================================================
@group_required('admin')
def table(request):
    context = {}

    # ===[Data]===
    datakurikulum = Kurikulum.objects.all()
        
    # ===[context]===
    context['datakurikulum'] = datakurikulum
    context['sidebar'] = 'admin.kurikulum'

    # ===[Render Template]===
    return render(request, 'adminpage/kurikulum/table.html', context)


@group_required('admin')
@transaction.atomic
def add(request):
    context = {}  

    # ===[Load Form]===
    context['title_text']     = "Tambah"
    context['kurikulumform']     = KurikulumCreateUpdateForm(request.POST or None, request.FILES or None)

    # ===[Insert Logic]===
    if request.POST:
        if context['kurikulumform'].is_valid():
            kurikulum = context['kurikulumform'].save()
            if kurikulum.is_active:
                Kurikulum.objects.exclude(id=kurikulum.id).update(is_active=False)
            messages.success(request, 'Data Berhasil Ditambahkan')
            return redirect('pendampingan:admin_kurikulum_table')
        else:
            messages.error(request, context['kurikulumform'].errors)

    # ===[context]===
    context['sidebar'] = 'admin.kurikulum'
    
    # ===[Render Template]===
    return render(request, 'adminpage/kurikulum/add.html', context)


@group_required('admin')
@transaction.atomic
def active_checked_json(request, id):
    try:
        kurikulum = Kurikulum.objects.get(id=id)                    
    except Kurikulum.DoesNotExist:
        return JsonResponse({'status': False, 'message': f'Kurikulum dengan id {id} tidak ditemukan'}, status=404)    
        
    json_data = json.loads(request.body)    
    kurikulum.is_active = json_data['is_checked']
    kurikulum.save()

    Kurikulum.objects.exclude(id=kurikulum.id).update(is_active=False)

    return JsonResponse({'status': True, 'message': f'Kurikulum dengan id {id} berhasil diupdate'}, status=200)



@group_required('admin')
@transaction.atomic
def delete(request, id):
    kurikulum = get_object_or_404(Kurikulum, pk=id)                
    print(kurikulum.id)
    print(kurikulum.is_active)
    if request.POST.get('delete'):
        if not kurikulum.is_active:
            kurikulum.delete()    
            messages.success(request, 'Data Berhasil Dihapus')    
        else:            
            messages.error(request, 'Kurikulum aktif tidak dapat dihapus')
    else:
        messages.error(request, 'Gunakan POST untuk hapus data')

    return redirect('pendampingan:admin_kurikulum_table')