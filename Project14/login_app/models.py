from django.db import models

class User(models.Model):
    email = models.EmailField()
    nom = models.CharField(max_length=100)
    cognom = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

def __str__(self):
    return self.nom
