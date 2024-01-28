from django.http import HttpResponse
from django.template import Template, Context

import datetime

def bienvenido1(request):
    return HttpResponse("Bienvenidos a la Comision 50200 - Clase Django")

def bienvenido2(request, nombre):
    respuesta = f"Bienvenidos {nombre} a la Comision 50200 - Clase Django"
    return HttpResponse(respuesta)

def bienvenido3(request):
    hoy = datetime.datetime.now()
    respuesta = f"""
    <html>
    <h1>Bienvenidos al curso de Django!!</h1>
    <h2>Esta es la comision 50200</h2>
    <h3>Hoy es {hoy} </h3>
    </html>
    """
    return HttpResponse(respuesta)

def bienvenido_template(request):
    miHtml = open("C:/CoderHouse PYTHON/Clase___17/proyecto1/proyecto1/plantillas/bienvenido.html")
    plantilla = Template(miHtml.read())
    miHtml.close()
    miContexto = Context()
    respuesta = plantilla.render(miContexto)
    return HttpResponse(respuesta)