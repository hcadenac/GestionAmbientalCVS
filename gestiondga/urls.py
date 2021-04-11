from django.contrib import admin
from django.urls import path
from gestiondga.views import saludo, inicio, busqueda, buscar
from gestiondga import views

urlpatterns = [
    path('', admin.site.urls, name='admin'),
    #path('saludo/', saludo),
    #path('inicio/', inicio),
    path('inicio', views.inicio, name='inicio'),
    path('busqueda', views.busqueda, name='busqueda'),
    path('buscar', views.buscar, name='buscar'),
    #path('consulta/', consulta),
    
]