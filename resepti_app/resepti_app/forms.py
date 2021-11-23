from django import forms
from django.db import models
from .models import Recipe, Category, Ingredient, Basic_ingredient, Recipe_Ingredient
from django.forms import ModelForm, widgets, TextInput, CheckboxInput
from ckeditor.widgets import CKEditorWidget
from ckeditor.fields import RichTextFormField


class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ['headline', 'body_text', 'image', 'categoryFK', 'basic_ingredient']
        widgets = {
            'headline': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Lisää otsikko'
            }),
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
            'basic_ingredient': widgets.CheckboxSelectMultiple(attrs={
            'class': '',
            })

        }



class Basic_ingredientForm(ModelForm):
    class Meta:
        model = Basic_ingredient
        fields = ['basicing_name']
        widgets = {
            'basicing_name': widgets.CheckboxSelectMultiple(attrs={
                'class': 'form-check-input',
            }),
        }
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['basicing_name'].required = False


class IngredientForm(ModelForm):
    class Meta:
        model = Ingredient
        fields = ['ing_name']
        widgets = {
            'ing_name': TextInput(attrs={
                'class': 'form-control',
                'id' : 'ingredient-form-left',
                'placeholder': 'Lisää raaka-aine',
            }),

        }


class Recipe_IngredientForm(ModelForm):
    class Meta:
        model = Recipe_Ingredient
        fields = ['amount']
        widgets = {
            'amount': TextInput(attrs={
                'class': 'form-control',
                'id' : 'ingredient-amount-form-right',
                'placeholder': 'Lisää ainemäärä',
            }),
        }


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


