from django.template import loader
from django.http import HttpResponse
from App_Familia.models import Familia

# Create your views here.

def guardar_familia_bd(request):
    mama = Familia(nombre_completo = "Maria Sanchez", fecha_nacimiento = "1980-02-10", no_identidad = 39163646)
    papa = Familia(nombre_completo = "Juan Perez", fecha_nacimiento = "1978-05-13", no_identidad = 45321458)
    hijo = Familia(nombre_completo = "Daniel Colorado", fecha_nacimiento = "1998-04-22", no_identidad = 1026554789)

    dic = {
        "nombre_mama": mama.nombre_completo,
        "dob_mama": mama.fecha_nacimiento,
        "id_mama": mama.no_identidad,
        "nombre_papa": papa.nombre_completo,
        "dob_papa": papa.fecha_nacimiento,
        "id_papa": papa.no_identidad,        
        "nombre_hijo": hijo.nombre_completo,
        "dob_hijo": hijo.fecha_nacimiento,
        "id_hijo": hijo.no_identidad
        }

    # Salva los objetos de la clase Familia en la DB
    mama.save()
    papa.save()
    hijo.save()

    plantilla = loader.get_template("template_1.html")
    doc = plantilla.render(dic)

    return HttpResponse(doc)
