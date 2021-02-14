from django.db import models

class Pizza(models.Model):

    nom = models.CharField(max_length=255)
    ingredients = models.CharField(max_length=400)
    prix = models.FloatField(default=0)
    veg = models.BooleanField(default=False)

    def __str__(self):
        return self.nom