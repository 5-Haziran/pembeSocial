"""
URL configuration for pembesocial project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from appMy.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='anasayfa'),
    path('kategori/<id>/',category,name='kategori'),
    path('detay/<id>/',detail,name="detay"),
    path('kayıtol/',register,name='kayıtol'),
    path('giris/',loginn,name="giris"),
    path('cıkıs/',logoutt,name='çıkış'),
    path('profil/',profil,name='profil'),
    path('like/<post_id>/',likeds,name='like'),
    path('trend/',trends,name='trend')
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

