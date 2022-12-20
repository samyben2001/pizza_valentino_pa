from django import forms
from django.forms import ModelForm
from .models import Allergene, Ingredient, Pizza

class EmailForm(forms.Form):
    sender = forms.EmailField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Votre E-mail'}))
    subject = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Sujet'}))
    message = forms.CharField(required=True, widget=forms.Textarea(attrs={'placeholder': 'Votre message'}))
