from django import forms
from django.db import models
from .models import Resepti, Category, Ingridient
from django.forms import ModelForm, widgets, TextInput, CheckboxInput


class ReseptiForm(ModelForm):
    class Meta:
        model = Resepti
        fields = ['headline', 'body_text', 'image', 'categoryFK', 'ingridientFK']
        widgets = {}

class IngridientForm(ModelForm):
    class Meta:
        model = Ingridient
        fields = ['ing_name']
        widgets = {}

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['cat_name']
        widgets = {}    