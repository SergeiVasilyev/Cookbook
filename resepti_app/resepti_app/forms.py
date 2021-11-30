from django import forms
from django.db import models
from .models import Recipe, Category, Ingredient
from django.forms import ModelForm, widgets, TextInput, CheckboxInput
from ckeditor.widgets import CKEditorWidget
from ckeditor.fields import RichTextFormField


class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ['headline', 'ingredient_quantity', 'body_text', 'image', 'categoryFK', 'ingredients']
        widgets = {
            'headline': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Lisää otsikko'
            }),
            'ingredient_quantity': RichTextFormField(),
            'body_text': RichTextFormField(),
            # 'body_text': widgets.Textarea(attrs={
            #     'class': 'form-control',
            #     'placeholder': 'lisää resepti'
            # }),
            'image': widgets.FileInput(attrs={
                'class': 'form-control-file',
                'title': 'Lisää kuva'
            }),
            'categoryFK': widgets.Select(attrs={
                'class': 'form-select',
            }),
            'ingredients': widgets.CheckboxSelectMultiple(attrs={
                'class': '',
            })
        }



class IngredientForm(ModelForm):
    class Meta:
        model = Ingredient
        fields = ['ing_name']
        widgets = {
            'ing_name': widgets.CheckboxSelectMultiple(attrs={
                'class': 'form-check-input',
            }),
        }
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['ing_name'].required = False


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['cat_name']
        widgets = {
            'cat_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Lisää ruokalaji'
            }),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat_name'].required = False


