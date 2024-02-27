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

from pendampingan.models import Lembaga, Karyawan, Kurikulum, MataKuliah
from pendampingan.forms.matakuliah_form import MataKuliahCreateUpdateForm
from services.apigateway import apigateway


# =====================================================================================================
#                                               LOAD PAGE
# =====================================================================================================
@group_required('admin')
def table(request, kurikulum_id):
    context = {}

    # ===[Data]===
    datakurikulum = get_object_or_404(Kurikulum, pk=kurikulum_id)
    datamatakuliah = MataKuliah.objects.filter(kurikulum=datakurikulum)
        
    # ===[context]===
    context['datakurikulum'] = datakurikulum
    context['datamatakuliah'] = datamatakuliah
    context['sidebar'] = 'admin.kurikulum'

    # ===[Render Template]===
    return render(request, 'adminpage/matakuliah/table.html', context)


@group_required('admin')
@transaction.atomic
def add(request, kurikulum_id):
    context = {}  

    # ===[Data]===
    datakurikulum = get_object_or_404(Kurikulum, pk=kurikulum_id)

    # ===[Load Form]===
    context['title_text']     = "Tambah"
    context['matakuliahform']     = MataKuliahCreateUpdateForm(request.POST or None, request.FILES or None)

    # ===[Insert Logic]===
    if request.POST:
        if context['matakuliahform'].is_valid():
            matakuliah = context['matakuliahform'].save(commit=False)
            matakuliah.kurikulum = datakurikulum
            matakuliah.save()            
            messages.success(request, 'Data Berhasil Ditambahkan')
            return redirect('pendampingan:admin_matakuliah_table', kurikulum_id=datakurikulum.id)
        else:
            messages.error(request, context['matakuliahform'].errors)

    # ===[context]===
    context['sidebar'] = 'admin.kurikulum'
    
    # ===[Render Template]===
    return render(request, 'adminpage/matakuliah/add.html', context)


@group_required('admin')
@transaction.atomic
def edit(request, kurikulum_id, id):
    context = {}  

    # ===[Data]===
    datamatakuliah = get_object_or_404(MataKuliah, pk=id)

    # ===[Load Form]===
    context['title_text']     = "Ubah"
    context['matakuliahform']     = MataKuliahCreateUpdateForm(request.POST or None, request.FILES or None, instance=datamatakuliah)

    # ===[Insert Logic]===
    if request.POST:
        if context['matakuliahform'].is_valid():
            matakuliah = context['matakuliahform'].save()                        
            messages.success(request, 'Data Berhasil Diubah')
            return redirect('pendampingan:admin_matakuliah_table', kurikulum_id=kurikulum_id)
        else:
            messages.error(request, context['matakuliahform'].errors)

    # ===[context]===
    context['sidebar'] = 'admin.kurikulum'
    
    # ===[Render Template]===
    return render(request, 'adminpage/matakuliah/add.html', context)


@group_required('admin')
@transaction.atomic
def sinkron(request, kurikulum_id):

    # ===[Data]===
    datakurikulum = get_object_or_404(Kurikulum, pk=kurikulum_id)
    
    # lmbg1005    
    apimatakuliah = apigateway.get(f'kurikulum_api/v1/prodi/lmbg1005/matakuliah?tahun={datakurikulum.tahun}')        
    try:
        if apimatakuliah['status']:
            for semester in apimatakuliah['data'].keys():
                for matakuliah in apimatakuliah['data'][semester]:                
                    MataKuliah.objects.update_or_create(
                        kode=matakuliah['kode_matakuliah'],
                        defaults={
                            "kurikulum": datakurikulum,
                            "nama": matakuliah["matakuliah"],
                            "jumlah_sks": matakuliah["jml_sks"],
                            "semester": matakuliah["semester"],
                            "deskripsi": matakuliah["deskripsi"],
                            "uniid_pengampu": matakuliah["uniid_pengampu"],                            
                        }
                    )
            messages.success(request, "Mata Kuliah berhasil disinkronkan dengan MyKurikulum")
        else:
            messages.error(request, apimatakuliah)
    except Exception as e:
        print(e)
        messages.error(request, str(e))

    return redirect('pendampingan:admin_matakuliah_table', kurikulum_id = datakurikulum.id)



@group_required('admin')
@transaction.atomic
def delete(request, kurikulum_id, id):
    matakuliah = get_object_or_404(MataKuliah, pk=id)                    
    if request.POST.get('delete'):        
        matakuliah.delete()    
        messages.success(request, 'Data Berhasil Dihapus')            
    else:
        messages.error(request, 'Gunakan POST untuk hapus data')

    return redirect('pendampingan:admin_matakuliah_table', kurikulum_id=kurikulum_id)