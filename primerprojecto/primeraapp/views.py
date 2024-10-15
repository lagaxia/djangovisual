from django.shortcuts import render
from django.http import HttpResponse
import datetime

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

def damefecha(request):
    fecha_actual = datetime.datetime.now() 
    fecha_formateada = fecha_actual.strftime("%d/%m/%Y %H:%M:%S")
    
    documento = f"""<html>
    <body>
    <h1>
    la fecha y hora actual es: {fecha_formateada}
    </h1>
    </body>
    </html>"""
    
    return HttpResponse(documento)

def calcula_edad(request,year,age):

    periodo = year - 2024
    edadFutura = age + periodo
    
    documento = f"""<html><body><h2>En el año {year} tu edad es {edadFutura}</h2></body></html>"""
    
    return HttpResponse(documento)