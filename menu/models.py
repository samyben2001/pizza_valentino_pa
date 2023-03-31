from django_resized import ResizedImageField
from distutils.command.upload import upload
from django.contrib import admin
from django.db import models
from django.forms import ModelForm, Textarea


class Ingredient(models.Model):
    nom = models.CharField(max_length=100)
    importance = models.IntegerField(default=0)

    def __str__(self):
        return self.nom

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['nom'], name='unique_ingredient_name')
        ]       

class Allergene(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['nom'], name='unique_allergene_name')
        ]

class Entree(models.Model):
    nom = models.CharField(max_length=100)
    image = ResizedImageField(size=[750, 650], quality=100, null=True, blank=True)
    prix = models.FloatField(default=0)
    allergene = models.ManyToManyField(Allergene, blank=True)

    def __str__(self):
        return self.nom

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['nom'], name='unique_entree_name')
        ]

class Pizza(models.Model):
    nom = models.CharField(max_length=100)
    image = ResizedImageField(size=[750, 650], quality=100, null=True, blank=True)
    ingredient = models.ManyToManyField(Ingredient)
    prix = models.FloatField(default=0)
    vegetarienne = models.BooleanField(default=False)
    suggestion = models.BooleanField(default=False)
    allergene = models.ManyToManyField(Allergene, blank=True)

    def get_ingredients(self):
        return ",\n".join([p.nom for p in sorted(self.ingredient.all(),key=lambda ingr: ingr.importance, reverse=True)])

    def __str__(self):
        return self.nom

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['nom'], name='unique_pizza_name')
        ]

class Pates(models.Model):
    nom = models.CharField(max_length=100)
    image = ResizedImageField(size=[750, 650], quality=100, null=True, blank=True)
    prix = models.FloatField(default=0)
    allergene = models.ManyToManyField(Allergene, blank=True)

    def __str__(self):
        return self.nom

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['nom'], name='unique_pates_name')
        ]
        verbose_name_plural  =  "Pates"

class Dessert(models.Model):
    nom = models.CharField(max_length=100)
    image = ResizedImageField(size=[750, 650], quality=100, null=True, blank=True)
    prix = models.FloatField(default=0)
    allergene = models.ManyToManyField(Allergene, blank=True)

    def __str__(self):
        return self.nom

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['nom'], name='unique_dessert_name')
        ]

class Boisson(models.Model):
    nom = models.CharField(max_length=100)
    image = ResizedImageField(size=[750, 650], quality=100, null=True, blank=True)
    prix = models.FloatField(default=0)
    allergene = models.ManyToManyField(Allergene, blank=True)

    def __str__(self):
        return self.nom

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['nom'], name='unique_boisson_name')
        ]

class Services(models.Model):
    nom = models.CharField(max_length=100)
    debut = models.TimeField(auto_now=False, auto_now_add=False)
    fin = models.TimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.nom
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['nom'], name='unique_services_name')
        ]

class Horaire(models.Model):
    jour = models.CharField(max_length=100)
    services = models.ManyToManyField(Services, blank=True)

    def __str__(self):
        return self.nom
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['jour'], name='unique_horaire_name')
        ]

class Annonce(models.Model):
    nom = models.CharField(max_length=100)
    actif = models.BooleanField()
    debut = models.DateField()
    fin = models.DateField()
    annonce = models.TextField()

    def __str__(self):
        return self.nom
    
    class Meta:
        widgets = {
            'annonce': Textarea(attrs={'cols': 80, 'rows': 10})
        }
        constraints = [
            models.UniqueConstraint(fields=['nom'], name='unique_annonce_name')
        ]