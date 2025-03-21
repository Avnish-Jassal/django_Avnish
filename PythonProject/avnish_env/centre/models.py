from django.db import models

# Create your models here.
class alumne(models.Model):
    nom = models.CharField(max_length=100)
    apellido1 = models.CharField(max_length=100)
    apellido2 = models.CharField(max_length=100)
    correu = models.EmailField(max_length=100)
    curs = models.CharField(max_length=10)
    modulsMatriculats = models.CharField(max_length=100)


class professor(models.Model):
    nom = models.CharField(max_length=100)
    apellido1 = models.CharField(max_length=100)
    apellido2 = models.CharField(max_length=100)
    correu = models.CharField(max_length=100)
    curs = models.CharField(max_length=10)
    tutor = models.CharField(max_length=100)
    moduls = models.IntegerField()