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
        verbose_name_plural = "01. Ingrédients"
        constraints = [
            models.UniqueConstraint(fields=['nom'], name='unique_ingredient_name')
        ]       

class Allergene(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name_plural = "02. Allergènes"
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
        verbose_name_plural = "03. Entrées"
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
        verbose_name_plural = "04. Pizzas"
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
        verbose_name_plural = "05. Pâtes"
        constraints = [
            models.UniqueConstraint(fields=['nom'], name='unique_pates_name')
        ]

class Dessert(models.Model):
    nom = models.CharField(max_length=100)
    image = ResizedImageField(size=[750, 650], quality=100, null=True, blank=True)
    prix = models.FloatField(default=0)
    allergene = models.ManyToManyField(Allergene, blank=True)

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name_plural = "06. Desserts"
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
        verbose_name_plural = "07. Boissons"
        constraints = [
            models.UniqueConstraint(fields=['nom'], name='unique_boisson_name')
        ]

class Service(models.Model):
    nom = models.CharField(max_length=100)
    debut = models.TimeField()
    fin = models.TimeField()

    def __str__(self):
        return self.nom
    
    class Meta:
        verbose_name_plural = "09. Services"
        constraints = [
            models.UniqueConstraint(fields=['nom'], name='unique_services_name')
        ]

class Horaire(models.Model):
    jour = models.CharField(max_length=100,
                            choices=[("Lundi","Lundi"),("Mardi","Mardi"),("Mercredi","Mercredi"),("Jeudi","Jeudi"),("Vendredi","Vendredi"),("Samedi","Samedi"),("Dimanche","Dimanche"),])
    
    services = models.ManyToManyField(Service, blank=True)

    def __str__(self):
        return self.jour
    
    class Meta:
        verbose_name_plural = "10. Horaire"
        ordering = ['pk']
        constraints = [
            models.UniqueConstraint(fields=['jour'], name='unique_horaire_name')
        ]

class Annonce(models.Model):
    nom = models.CharField(max_length=100)
    actif = models.BooleanField()
    debut = models.DateField()
    fin = models.DateField()
    annonce = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nom
    
    class Meta:
        verbose_name_plural = "08. Annonces"
        constraints = [
            models.UniqueConstraint(fields=['nom'], name='unique_annonce_name')
        ]