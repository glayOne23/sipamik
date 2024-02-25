"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve
from django.contrib.auth.decorators import login_required
from project.views import dashboard, authentication
import django_cas_ng.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('hijack/', include('hijack.urls')),
    path('', login_required(dashboard.index), name='homepage'),
    path('adminpage/dashboard/', login_required(dashboard.index), name='dashboard'),    

    path('signin/',      authentication.signin,                               name='signin'),
    path('signout/',     authentication.signout,                              name='signout'),           
    path('login_cas/', django_cas_ng.views.LoginView.as_view(),    name='cas_ng_login'), # Default Django CAS Login
    path('logout_cas/',  django_cas_ng.views.LogoutView.as_view(),   name='cas_ng_logout'),
    path('callback/',    django_cas_ng.views.CallbackView.as_view(), name='cas_ng_proxy_callback'),

    path('adminpage/pendampingan/', include('pendampingan.urls', namespace='pendampingan')),

]

if settings.ON_PRODUCTION:
    urlpatterns += [
        re_path(r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
        re_path(r"^static/(?P<path>.*)$", serve, {"document_root": settings.STATIC_ROOT}),
    ]
else:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)