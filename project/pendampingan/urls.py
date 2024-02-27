from django.urls import path, include
from django.contrib.auth.decorators import login_required

from pendampingan.views import lembaga, karyawan, kurikulum, matakuliah

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
        path('<int:id>/active_checked_json/',                login_required(karyawan.active_checked_json),             name='admin_karyawan_active_checked_json'),
        # path('deletelist/',                        login_required(category.deletelist),        name='category_deletelist'),
    ])),    
    path('admin/kurikulum/', include([
        # =================================================[ LOAD PAGE ]=================================================
        path('table/',                             login_required(kurikulum.table),             name='admin_kurikulum_table'),
        path('add/',                               login_required(kurikulum.add),               name='admin_kurikulum_add'),
        # path('edit/<int:id>/',                     login_required(category.edit),              name='category_edit'),
        path('<int:id>/delete/',                login_required(kurikulum.delete),             name='admin_kurikulum_delete'),

        # ==================================================[ SERVICE ]==================================================
        path('<int:id>/active_checked_json/',                login_required(kurikulum.active_checked_json),             name='admin_kurikulum_active_checked_json'),        

        path('<int:kurikulum_id>/matakuliah/', include([
            # =================================================[ LOAD PAGE ]=================================================
            path('table/',                             login_required(matakuliah.table),             name='admin_matakuliah_table'),
            path('add/',                               login_required(matakuliah.add),               name='admin_matakuliah_add'),
            path('sinkron/',                           login_required(matakuliah.sinkron),             name='admin_matakuliah_sinkron'),
            path('edit/<int:id>/',                     login_required(matakuliah.edit),              name='admin_matakuliah_edit'),
            path('<int:id>/delete/',                login_required(matakuliah.delete),             name='admin_matakuliah_delete'),            
        ])),        
    ])),    
]
