from django.db import models

class Network(models.Model):
    company=models.JSONField()
    gbfs_href=models.CharField(max_length=200)
    href=models.CharField(max_length=200)
    ids=models.CharField(max_length=200)
    location=models.JSONField()
    name=models.CharField(max_length=200)
    stations=models.JSONField()

