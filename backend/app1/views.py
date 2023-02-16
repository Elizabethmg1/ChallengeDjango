from contextvars import Context
from pipes import Template
from django.shortcuts import render
from django.template import Template, Context
from .scraping import converter_json
from app1.models import Proyecto
from django.http import HttpResponse
import json

def proyecto(self):
    diccionario = {}
    dict=json.loads(converter_json())
    print(dict)
    for i in dict:
        proyecto = Proyecto(numero=i["numero"],nombre=i["nombre"],region=i["region"],tipologia=i["tipologia"],inversion=i["inversion"],fecha=i["fecha"],estado=i["estado"])
        proyecto.save()

        diccionario[str(proyecto.nombre)]={"numero:":proyecto.numero,"nombre":proyecto.nombre,"tipo":proyecto.tipo,"region":proyecto.region,"tipologia":proyecto.tipologia,"titular":proyecto.titular,"inversion":proyecto.inversion,"fecha":proyecto.fecha,"estado":proyecto.estado}
    
    lista = []
    for k in diccionario.values():
        lista.append(k)

    diccionario['values']=lista

    mihtml=open('C:/Users/Micaela/Desktop/Challenge Django/ChallengeDjango/backend/planillas/template1.html')
    plantilla = Template(mihtml.read())
    mihtml.close()
    mi_contexto=Context(diccionario)
    documento= plantilla.render(mi_contexto)
    return HttpResponse(documento)

