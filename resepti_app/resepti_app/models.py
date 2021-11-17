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

class Basic_ingredient(models.Model):
    basicing_name = models.CharField(max_length=200)
    class Meta:
        ordering = ('basicing_name',)

    def __str__(self):
        return self.basicing_name
    

class Recipe(models.Model):
    headline = models.CharField(max_length=300)
    body_text = RichTextField(blank=True, null=True)
    # body_text = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='images/')
    # slug = AutoSlugField(populate_from='headline')
    categoryFK = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True) #SET_DEFAULT , to_field='name'
    basic_ingredient = models.ManyToManyField(Basic_ingredient, related_name='recipes') # recipe_set

    def __str__(self):
        return f"ReseptiList: {self.id} | {self.headline}"
    
class Recipe_Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, blank=True, null=True)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, blank=True, null=True)
    amount = models.CharField(max_length=50)

    def __str__(self):
        return f"Resipe_Ingredient: {self.recipe_id} | {self.ingredient_id} | {self.amount}"