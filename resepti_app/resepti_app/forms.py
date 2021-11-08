from django import forms
from django.db import models
from .models import Recipe, Category, Ingredient
from django.forms import ModelForm, widgets, TextInput, CheckboxInput
from ckeditor.widgets import CKEditorWidget
from ckeditor.fields import RichTextFormField


class RecipeForm(ModelForm):
    class Meta:
        # body_text = forms.CharField(widget=CKEditorWidget())
        model = Recipe
        fields = ['headline', 'body_text', 'image', 'categoryFK', 'ingredients']
        widgets = {
            'headline': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'lisää otsikko'
            }),
            'body_text': RichTextFormField(),
            # 'body_text': widgets.Textarea(attrs={
            #     'class': 'form-control',
            #     'placeholder': 'lisää resepti'
            # }),
            'image': widgets.FileInput(attrs={
                'class': 'form-control-file',
                'title': 'lisää kuva'
            }),
            'categoryFK': widgets.Select(attrs={
                'class': 'form-select',
            }),
            'ingredients': widgets.CheckboxSelectMultiple(attrs={
                'class': '',
            })
        }

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['categoryFK'].required = False
    #     self.fields['ingridientFK'].required = False


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
                'placeholder': 'lisää ruokalaji'
            }),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat_name'].required = False

# class Recipe_IngredientForm(ModelForm):
#     class Meta:
#         model = Recipe_Ingredient
#         fields = ['recipeFK', 'ingredFK']
#         widgets = {
#             'recipeFK': widgets.CheckboxInput(attrs={
#                 'class': 'form-check-input',
#             }),
#         }
