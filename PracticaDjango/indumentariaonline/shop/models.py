from django.db import models


class Remera(models.Model):
    marca = models.CharField(max_length=128)
    talle = models.IntegerField()
    color = models.CharField(max_length=128)
    lisa = models.BooleanField()
    genero = models.IntegerField()

