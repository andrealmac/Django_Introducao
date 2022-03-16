
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls), #andre.com.br/admin/
    path('', include('hello.urls')), #andre.com.br/dominio raiz usa o include
]
