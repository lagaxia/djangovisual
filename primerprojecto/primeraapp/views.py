from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def saludo (request):
    
    documento = """<html>
    <body>
    <h1>
    Hola alumnos esta es nuestra primera pagina django
    </h1>
    </body>
    </html>"""
    
    return HttpResponse(documento)
    
    
def despedida(request):
    return HttpResponse("Adios a alumnos de djando")

def mostrar_template(request):
    contexto = {
        'nombre': 'Juan',
        'edad': 30
    }
    return render(request, 'index.html', contexto)