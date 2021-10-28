from django import forms
from django.db import models
from .models import Resepti, Category, Ingridient
from django.forms import ModelForm, widgets, TextInput, CheckboxInput


class ReseptiForm(ModelForm):
    class Meta:
        model = Resepti
        fields = ['headline', 'body_text', 'image', 'categoryFK', 'ingridientFK']
        widgets = {
            'headline': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'lisää otsikko'
            }),
            'body_text': widgets.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'lisää resepti'
            }),
            'image': widgets.FileInput(attrs={
                'class': 'form-control-file',
                'title': 'lisää kuva'
            }),
            'categoryFK': widgets.Select(attrs={
                'class': 'form-select',
            }),
            'ingridientFK': widgets.Select(attrs={
                'class': 'form-select',
            }),
        }

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['categoryFK'].required = False
    #     self.fields['ingridientFK'].required = False


class IngridientForm(ModelForm):
    class Meta:
        model = Ingridient
        fields = ['ing_name']
        widgets = {
            'ing_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'lisää raaka-aine'
            }),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['ing_name'].required = False


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['cat_name']
        widgets = {
            'cat_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'lisää ruokalaji'
            }),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat_name'].required = False
