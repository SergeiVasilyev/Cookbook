from django.db import models
from django.db.models.fields.related import ManyToManyField
# from autoslug import AutoSlugField
from ckeditor.fields import RichTextField



class Category(models.Model):
    cat_name = models.CharField(max_length=200)
    
    def __str__(self):
        return f"Category: {self.id} | {self.cat_name}"
    
class Ingredient(models.Model):
    ing_name = models.CharField(max_length=200)
    class Meta:
        ordering = ('ing_name',)

    def __str__(self):
        return self.ing_name
    
class Recipe(models.Model):
    headline = models.CharField(max_length=300)
    ingredient_quantity = RichTextField(blank=True, null=True)
    body_text = RichTextField(blank=True, null=True)
    # body_text = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='images/')
    # slug = AutoSlugField(populate_from='headline')
    categoryFK = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True) #SET_DEFAULT , to_field='name'
    ingredients = models.ManyToManyField(Ingredient, related_name='recipes') # recipe_set

    def __str__(self):
        return f"ReseptiList: {self.id} | {self.headline}"
    
