from django.db import models
from django.db.models.fields.related import ManyToManyField
# from autoslug import AutoSlugField

class Category(models.Model):
    cat_name = models.CharField(max_length=200)
    
    def __str__(self):
        return f"Category: {self.id} | {self.cat_name}"
    
class Ingredient(models.Model):
    ing_name = models.CharField(max_length=200)

    def __str__(self):
        return self.ing_name
    
class Recipe(models.Model):
    headline = models.CharField(max_length=300)
    body_text = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='images/')
    # slug = AutoSlugField(populate_from='headline')
    categoryFK = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True) #SET_DEFAULT , to_field='name'
    ingredients = models.ManyToManyField(Ingredient, related_name='recipes') # recipe_set

    def __str__(self):
        return f"ReseptiList: {self.id} | {self.headline}"
    
# class Recipe_Ingredient (models.Model):
#     recipeFK = models.ForeignKey(Recipe, on_delete=models.CASCADE, blank=True, null=True)
#     ingredFK = models.ForeignKey(Ingredient, on_delete=models.CASCADE, blank=True, null=True)
#     amount = models.FloatField()
#     unit = models.CharField()
#     def __str__(self):
#         return f"Recipe_Ingredient: {self.id} | {self.recipeFK} | {self.ingredFK}"

