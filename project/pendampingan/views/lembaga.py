from django.shortcuts import render, redirect
# from apps.services.decorators import group_required
from django.contrib import messages
from django.db import transaction

from django.urls import reverse
from json import dumps

from services.decorators import group_required

from pendampingan.models import Lembaga
from services.apigateway import apigateway


# =====================================================================================================
#                                               LOAD PAGE
# =====================================================================================================
@group_required('admin')
def table(request):
    context = {}

    # ===[Data]===
    datalembaga = Lembaga.objects.all().order_by('jenis_id')
        
    # ===[context]===
    context['datalembaga'] = datalembaga
    context['sidebar'] = 'admin.lembaga'    

    # ===[Render Template]===
    return render(request, 'adminpage/lembaga/table.html', context)


@group_required('admin')
@transaction.atomic
def sinkron(request):

    apilembaga = apigateway.get('umar/v4/lembaga')
    try:
        if apilembaga['status']:
            for lembaga in apilembaga['data']:
                Lembaga.objects.update_or_create(
                    uniid=lembaga['uniid'],
                    defaults={
                        "nama": lembaga['nama'],
                        "namasingkat": lembaga['namasingkat'],
                        "superunit": lembaga['superunit'],
                        "namasuper": lembaga['namasuper'],
                        "jenis_id": lembaga['jenis_id'],
                        "jenis": lembaga['jenis']
                    }
                )
            messages.success(request, "Lembaga berhasil disinkronkan dengan SIHRD")
        else:
            messages.error(request, apilembaga)
    except Exception as e:
        print(e)
        messages.error(request, str(e))


    return redirect('pendampingan:admin_lembaga_table')