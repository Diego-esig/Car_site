from django.db import models


# Create your models here.

class Produit(models.Model):
    marque = models.CharField(max_length=200)
    modele = models.CharField(max_length=200)
    categorie = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    prix = models.FloatField()
    image = models.CharField(max_length=200)
