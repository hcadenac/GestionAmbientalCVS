from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context
from gestiondga.models import Empresa

# Create your views here.
def saludo(request):
    doc_externo = open("C:/Users/Hugo/Desktop/CursoDjango/gestionAmbiental/modulos/plantillas/barra.html")
    plt = Template(doc_externo.read())
    doc_externo.close()
    ctx= Context()
    documento= plt.render(ctx)
    
    return HttpResponse(documento)

def inicio(request):
   empresa= Empresa.objects.all()
   return render(request, "inicio.html", {"empresa":empresa})

def busqueda(request):
    return render(request, "buscar.html")

def buscar(request):
    
    if request.GET['prd']:
        mynit= request.GET['prd']
        #empresa= Empresa.objects.filter(nit__icontains=mynit)
        empresa= Empresa.objects.select_related().filter(nit=mynit)
        return render(request, "buscar.html", {"empresa":empresa, "query":mynit})
    else:
        mensaje= "No se ha seleccionado nada ..GONORREA..."

    #return HttpResponse(mensaje)
    return render(request, "buscar.html")


