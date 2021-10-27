from django.contrib import admin

from .models import Resepti, Ingridient, Category

#@admin.register(Todolist)

class TodolistAdmin(admin.ModelAdmin):
    fields = ['headline', 'body_text', 'image', 'categoryFK', 'ingridientFK']

class IngridientAdmin(admin.ModelAdmin):
    fields = ['ing_name']

class CategoryAdmin(admin.ModelAdmin):
    fields = ['cat_name']


admin.site.register(Resepti, TodolistAdmin)
admin.site.register(Ingridient)
admin.site.register(Category)