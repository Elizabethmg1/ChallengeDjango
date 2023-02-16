from contextvars import Context
from pipes import Template
from django.shortcuts import render
from django.template import Template, Context
from .API import devolver_json
from app.models import Network
from django.http import HttpResponse

def network(self):
    info=devolver_json(self)
    info_network= info["network"]
    network = Network(company=info_network['company'],gbfs_href=info_network['gbfs_href'],href=info_network['href'],ids=info_network['id'],location=info_network["location"],name=info_network['name'],stations=info_network['stations'])
    network.save()

    mihtml=open('C:/Users/Micaela/Desktop/Challenge Django/ChallengeDjango/backend/planillas/template.html')
    plantilla = Template(mihtml.read())
    mihtml.close()
    dict_network={"company":network.company,"gbfs_href":network.gbfs_href,"href":network.href,"id":network.ids,"location":network.location,"name":network.name,"stations":network.stations}
    mi_contexto=Context(dict_network)
    documento= plantilla.render(mi_contexto)
    return HttpResponse(documento)
    

