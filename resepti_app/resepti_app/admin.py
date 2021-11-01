from django.contrib import admin

from .models import Recipe, Ingredient, Category

#@admin.register(Recipe)

class RecipeAdmin(admin.ModelAdmin):
    fields = ['headline', 'body_text', 'image', 'categoryFK']

class IngredientAdmin(admin.ModelAdmin):
    fields = ['ing_name']

class CategoryAdmin(admin.ModelAdmin):
    fields = ['cat_name']


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient)
admin.site.register(Category)
