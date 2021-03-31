from django.contrib import admin
from gestiondga.models import *

# Register your models here.

class EmpresaAdmin(admin.ModelAdmin):
    list_display=("nit", "razon_social", "municipio", "direccion", "cedula_representante")
    search_fields=("nit","razon_social")
    list_filter=("fecha_creacion_dga", "municipio")
    
class DgaAdmin(admin.ModelAdmin):
    list_display=("id_dga", "nombre_responsable", "nivel_estudio", "titulo", "cargo")
    search_fields=("nombre_responsable", "nivel_estudio", "cargo")

class RepresentanteAdmin(admin.ModelAdmin):
    list_display=("cedula", "nombre_rep")
    search_fields=("cedula",)

admin.site.register(Representante, RepresentanteAdmin)
admin.site.register(Municipio)
admin.site.register(Empresa, EmpresaAdmin)
admin.site.register(DGA, DgaAdmin)
admin.site.register(Funcionario)
admin.site.register(Seguimiento)
