from django.http import HttpResponse
from django.template import Template, Context, loader

import datetime, random
from miapp.models import *

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
    hoy = datetime.datetime.now()
    nombre = "Amadeus"
    apellido = "Mozart"
    notas = [10, 9, 8, 9, 10]
    diccionario = {"nombre": nombre, "apellido": apellido,
                   "autor": "Pablo Suajes", "hoy": hoy, "notas": notas}
    
    plantilla = loader.get_template('bienvenido.html')
    respuesta = plantilla.render(diccionario)
    return HttpResponse(respuesta)

def nuevo_curso(request):
    nro_comision = random.randint(1,99999)
    str_nombre = "Python " + str(nro_comision)
    curso = Curso(nombre=str_nombre, comision=nro_comision)
    curso.save()
    documento = f"<html><h1>Se guardo {str_nombre} y comision {nro_comision}</h1></html>"
    return HttpResponse(documento)