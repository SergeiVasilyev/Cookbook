from django.db import models
from django.db.models.fields.related import ManyToManyField
# from autoslug import AutoSlugField
from ckeditor.fields import RichTextField



class Category(models.Model):
    cat_name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.cat_name
    
class Ingredient(models.Model):
    ing_name = models.CharField(max_length=200, unique=True)
    class Meta:
        ordering = ('ing_name',)

    def __str__(self):
        return self.ing_name

class Basic_ingredient(models.Model):
    basicing_name = models.CharField(max_length=200, blank=True, null=True)
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
    basic_ingredient = models.ManyToManyField(Basic_ingredient, related_name='recipes', blank=True) # recipe_set

    def __str__(self):
        return f"ReseptiList: {self.id} | {self.headline}"


class Recipe_Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, blank=True, null=True)
    ing_name = models.CharField(max_length=200)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, blank=True, null=True)
    amount = models.CharField(max_length=50)

    class Meta:
        ordering = ('id',)

    def save(self, *args, **kwargs):
        if self.ing_name and not self.ingredient:
            (ingredient, _created) = Ingredient.objects.get_or_create(ing_name=self.ing_name)
            self.ingredient = ingredient
        super().save(*args, **kwargs)

    def __str__(self):
        return self.amount