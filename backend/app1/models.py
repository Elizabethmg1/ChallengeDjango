from django.db import models

class Proyecto(models.Model):
    numero=models.IntegerField()
    nombre=models.CharField(max_length=200)
    tipo=models.CharField(max_length=200)
    region=models.CharField(max_length=200)
    tipologia=models.CharField(max_length=200)
    titular=models.CharField(max_length=200)
    inversion=models.CharField(max_length=200)
    fecha=models.CharField(max_length=200)
    estado=models.CharField(max_length=200)
