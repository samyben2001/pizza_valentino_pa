from django.contrib import admin
from django.db import models
from django.forms import CheckboxSelectMultiple
from django.contrib.auth.models  import  Group 
from .models import Ingredient,Allergene,Entree,Pizza,Pates,Dessert,Boisson,Services,Horaire,Annonce

admin.site.unregister(Group)  

class ingredientAdmin(admin.ModelAdmin):
    list_display=('nom',)
    ordering = ['-importance', 'nom']
    
class allergeneAdmin(admin.ModelAdmin):
    list_display=('nom',)
    ordering = ['nom']

class entreeAdmin(admin.ModelAdmin):
    list_display=('nom','prix')

class  pizzaAdmin(admin.ModelAdmin):
    list_display=('nom', 'get_ingredients','prix')  
    ordering = ['prix']
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }

class patesAdmin(admin.ModelAdmin):
    list_display=('nom','prix')
    ordering = ['prix']
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }

class dessertsAdmin(admin.ModelAdmin):
    list_display=('nom','prix')
    ordering = ['prix']
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }

class boissonAdmin(admin.ModelAdmin):
    list_display=('nom','prix')
    ordering = ['prix']
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }

class servicesAdmin(admin.ModelAdmin):{}
     

class horaireAdmin(admin.ModelAdmin):
        formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }

class annonceAdmin(admin.ModelAdmin):{}

admin.site.register(Ingredient, ingredientAdmin)
admin.site.register(Allergene, allergeneAdmin)
admin.site.register(Entree, entreeAdmin)
admin.site.register(Pizza, pizzaAdmin)
admin.site.register(Pates, patesAdmin)
admin.site.register(Dessert, dessertsAdmin)
admin.site.register(Boisson, boissonAdmin)
admin.site.register(Services, servicesAdmin)
admin.site.register(Horaire, horaireAdmin)
admin.site.register(Annonce, annonceAdmin)
