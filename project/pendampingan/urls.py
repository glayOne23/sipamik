from django.urls import path, include
from django.contrib.auth.decorators import login_required

from pendampingan.views import lembaga, karyawan

app_name = 'pendampingan'

urlpatterns = [    
    path('admin/lembaga/', include([
        # =================================================[ LOAD PAGE ]=================================================
        path('table/',                             login_required(lembaga.table),             name='admin_lembaga_table'),
        path('sinkron/',                           login_required(lembaga.sinkron),             name='admin_lembaga_sinkron'),
        # path('add/',                             login_required(category.add),               name='category_add'),
        # path('edit/<int:id>/',                   login_required(category.edit),              name='category_edit'),

        # ==================================================[ SERVICE ]==================================================        
        # path('deletelist/',                        login_required(category.deletelist),        name='category_deletelist'),
    ])),
    path('admin/karyawan/', include([
        # =================================================[ LOAD PAGE ]=================================================
        path('table/',                             login_required(karyawan.table),             name='admin_karyawan_table'),
        path('sinkron/',                             login_required(karyawan.sinkron),             name='admin_karyawan_sinkron'),
        # path('add/',                               login_required(karyawan.add),               name='admin_karyawan_add'),
        # path('edit/<int:id>/',                     login_required(category.edit),              name='category_edit'),

        # ==================================================[ SERVICE ]==================================================
        path('<int:id>/active_checked_json/',                login_required(karyawan.active_checked_json),             name='admin_lembaga_active_checked_json'),
        # path('deletelist/',                        login_required(category.deletelist),        name='category_deletelist'),
    ])),    
]
