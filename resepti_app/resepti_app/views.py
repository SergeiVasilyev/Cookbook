import os
from django.conf import settings
from django.http import response
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import HttpResponse, HttpResponseRedirect, render
from .forms import RecipeForm, CategoryForm, IngredientForm, Basic_ingredientForm, Recipe_IngredientForm
from django.core.files.storage import FileSystemStorage
from .models import Recipe, Ingredient, Category, Basic_ingredient, Recipe_Ingredient
from django.db.models import Q
from django.forms import formset_factory, modelformset_factory
from django.forms.models import inlineformset_factory
import re


def index (request):
    recipes = Recipe.objects.all()
    
    context = {
        'recipes': recipes,
        
    }  
    return render(request, 'resepti_app/index.html', context)

def add_resepti2(request): # Testi funktio: miten formset factory toimii
    IngredientFormSet = modelformset_factory(Ingredient, form=IngredientForm, extra=1) #modelformset_factory
    if request.method == 'POST':
        print('request.POST ', request.POST)
        formset = IngredientFormSet(request.POST)
        print(formset.cleaned_data)
        if formset.is_valid():
            formset.save()
            print('SAVED')
            for form in formset:
                print(form.cleaned_data)
            return redirect('add_resepti')
    else:
        formset = IngredientFormSet(request.POST or None, queryset=Ingredient.objects.none())
        context = {
            'formset': formset,
        }
    return render(request, 'resepti_app/add_resepti.html', context)



def add_resepti(request):
    IngredientFormSet = modelformset_factory(Ingredient, form=IngredientForm) #modelformset_factory
    Recipe_IngredientFormSet = modelformset_factory(Recipe_Ingredient, form=Recipe_IngredientForm)
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        cat = CategoryForm(request.POST)
        ingredient = IngredientForm(request.POST)
        amount = Recipe_IngredientForm(request.POST)
        print('request.POST ', request.POST)
        formset = IngredientFormSet(request.POST)
        formset_amount = Recipe_IngredientFormSet(request.POST)
        print(formset_amount.cleaned_data)
        # print('REQUEST:: ', form.base_fields)
        if cat.is_valid() and cat.cleaned_data['cat_name']:
            category = cat.save()
        else:
            category = None
        
        
        if form.is_valid():
            if category:
                Resepti_item = form.save(commit=False)
                Resepti_item.categoryFK = category
                Resepti_item.save()
                form.save()
                print('category ', category)
            else:
                Resepti_item = form.save()
            
        if formset.is_valid() and formset_amount.is_valid():
            # Нужно чтобы далее использовать как инстнас для записи в поле ingredient
            instance = formset.save() # Tarvitsee jos me halutaan tallentaa Recipe_Ingredientiin
            # Если не использовать commit=False записывает в базу данных 2 раза
            instance_amount = formset_amount.save(commit=False) # Jos poistaa commit=False, se tallentaa 2 kertaa!!!!!!!!?????
            print('SAVED')
            for form, amount in zip(instance, instance_amount): # 2 sykliä 
                print('form ', form)
                print('amount', amount)
                # Tallennetaan tietokantaan kaikki Ingredienti ja Amount kentat
                ing_rec = Recipe_Ingredient(amount=amount, ingredient=form, recipe=Resepti_item, ing_name=form) # ingredient=form INSTANCE ERROR
                ing_rec.save()
                # print(ing_rec)

        # Sivun indeksi etsiminen
        item = Recipe.objects.latest('id')
        print('Last item', item.id)
        return redirect(f'/resepti/{item.id}')
        # return redirect('add_resepti')
        

    form = RecipeForm()
    form_basic_ingrediet = Basic_ingredientForm()
    form_category = CategoryForm()
    form_ingredient = IngredientForm()
    form_amount = Recipe_IngredientForm()
    formset = IngredientFormSet(request.POST or None, queryset=Ingredient.objects.none())
    formset_amount = Recipe_IngredientFormSet(request.POST or None, queryset=Recipe_Ingredient.objects.none())
    context = {
        'form': form,
        'form_basic_ingrediet': form_basic_ingrediet,
        'form_category': form_category,
        'form_ingredient': form_ingredient,
        'form_amount': form_amount,
        'formset': formset,
        'formset_amount': formset_amount,
    }
        
    return render(request, 'resepti_app/add_resepti.html', context)
  
  
def success(request):
    return HttpResponse('successfully uploaded2')

def resepti(request, idx):
    recipe_ingredients = Recipe_Ingredient.objects.filter(recipe_id=idx)
    print(recipe_ingredients)
    recipe = Recipe.objects.get(id=idx)
    context = {
        'recipe': recipe,
        'recipe_ingredients': recipe_ingredients,
    }
    return render(request, 'resepti_app/resepti.html', context) 

def search(request):  
    if request.method == 'GET':
        print('search_form: ', request.GET.get('search_form'))
        request_form = request.GET.get('search_form')
        items = Basic_ingredient.objects.filter(basicing_name__icontains=request_form)
        category_items = Category.objects.filter(cat_name__icontains=request_form)
        body_text_items = Recipe.objects.filter(body_text__icontains=request_form)
        headline_items = Recipe.objects.filter(headline__icontains=request_form)
        if not items.exists() and not body_text_items.exists() and not headline_items.exists() and not category_items.exists():
            recipes = None
            print('recipes ', None)
        else:
            recipes = Recipe.objects.filter(Q(basic_ingredient__in=items) | Q(body_text__icontains=request_form) | Q(headline__icontains=request_form) | Q(categoryFK__in=category_items)).distinct()
            print('recipes ', recipes)
    context = {
        'recipes': recipes,
    }
    return render(request, 'resepti_app/index.html', context)

def search_category(request, cat_id):
    if request.method == 'GET':
        recipes = Recipe.objects.filter(categoryFK=cat_id)
        print('items', recipes)

        # Tarkistetaan url path, jos url /search_category/\d+/ palautetaan True search sivuun, ja laitetaan kategoria search kenttään
        url_ex = "^/search_category/\d+/$"
        m = re.match(url_ex, request.path)
        print('match ', m)
        url = False
        if m:
            url = True
    context = {
        'recipes': recipes,
        'url': url,
    }
    return render(request, 'resepti_app/index.html', context)


def edit_resepti2(request, id):
    data_item = Recipe.objects.get(id=id)
    form = RecipeForm(instance=data_item)
    Recipe_IngredientFormSet = modelformset_factory(Recipe_Ingredient, form=Recipe_IngredientForm, extra=0)
    IngredientFormSet = modelformset_factory(Ingredient, form=IngredientForm, extra=0, fields=('ing_name',))
    
    if request.method == 'POST':
        print('REQUEST')
        formset = IngredientFormSet(request.POST, prefix='ingredient')
        if formset.is_valid():
            print('SAVED')
            formset.save()
    else:
        formset = IngredientFormSet(queryset=Ingredient.objects.filter(id__range=[75, 77]), prefix='ingredient')
    context = {
        'formset': formset,
        # 'form': form,
    }
    return render(request, 'resepti_app/edit_resepti.html', context)


def edit_resepti(request, id): 
    data_item = Recipe.objects.get(id=id)
    form = RecipeForm(instance=data_item)

    Recipe_IngredientFormSet = inlineformset_factory(Recipe, Recipe_Ingredient, Recipe_IngredientForm, can_delete=False, fields="__all__", extra=0)
    if request.method == 'POST':
        #ingr_formset = IngredientFormSet(request.POST, prefix='ingredient')
        form = RecipeForm(request.POST, request.FILES, instance=data_item)
        formset = Recipe_IngredientFormSet(request.POST, prefix='recipe-ing', instance=data_item)
        if form.is_valid() and formset.is_valid: # and ingr_formset.is_valid:
            print('FORM is VALID')
            form.save()
            formset.save()
            #print('SAVED EDITING', request.POST.get("ingredient-0-ing_name"))
            print(list(request.POST.items()))
            return redirect('/resepti/' + str(id))
    else:
        formset = Recipe_IngredientFormSet(instance=data_item, prefix='recipe-ing')

    context = {
        'form': form,
        'formset': formset,
    }
    return render(request, 'resepti_app/edit_resepti.html', context)


def poista_resepti (request, idx): # Добавить удаление ингредиентов!
    item = Recipe.objects.get(id=idx)

    recipe_ingredient_items = Recipe_Ingredient.objects.filter(recipe=item)
    for recipe_ingredient_item in recipe_ingredient_items:
        ingredient_item = Ingredient.objects.filter(id=recipe_ingredient_item.ingredient_id)
        ingredient_item.delete()
        print('ingredient_item ', ingredient_item)

    print(item.image.path)
    item.delete()
    try:
        os.remove(item.image.path)
    except:
        return redirect ('home')
    return redirect ('home')


# ---------------------------------------------------------------------






# def add_resepti(request):
#     if request.method == 'POST':
#         form = RecipeForm(request.POST, request.FILES)
#         cat = CategoryForm(request.POST)
#         ingredient = IngredientForm(request.POST)
#         amount = Recipe_IngredientForm(request.POST)
#         #print('REQUEST:: ', form.base_fields)
#         if cat.is_valid() and cat.cleaned_data['cat_name']:
#             category = cat.save()
#         else:
#             category = None
        
#         if form.is_valid():
#             if category:
#                 Resepti_item = form.save(commit=False)
#                 Resepti_item.categoryFK = category
#                 Resepti_item.save()
#                 form.save()
#                 print('category ', category)
#             else:
#                 Resepti_item = form.save()

#             ing = ingredient.save()
#             ing_rec = Recipe_Ingredient(amount=amount, ingredient=ing, recipe=Resepti_item)
#             ing_rec.save()
#             print(ing_rec)

#             return redirect('add_resepti')



#     form = RecipeForm()
#     form_basic_ingrediet = Basic_ingredientForm()
#     form_category = CategoryForm()
#     form_ingredient = IngredientForm()
#     form_amount = Recipe_IngredientForm()
#     context = {
#         'form': form,
#         'form_basic_ingrediet': form_basic_ingrediet,
#         'form_category': form_category,
#         'form_ingredient': form_ingredient,
#         'form_amount': form_amount,
#     }
        
#     return render(request, 'resepti_app/add_resepti.html', context)
  






# def add_resepti(request):
    
#     if request.method == 'POST':
#         form = RecipeForm(request.POST, request.FILES)
#         ing = IngredientForm(request.POST)
#         cat = CategoryForm(request.POST)
#         #print('REQUEST:: ', form.base_fields)

#         if cat.is_valid() and cat.cleaned_data['cat_name']:
#             category = cat.save()
#         else:
#             category = None

#         if ing.is_valid() and ing.cleaned_data['ing_name']:
#             ingredient = ing.save()
#         else:
#             ingredient = None
        
#         if form.is_valid():
#             if ingredient:
#                 Resepti_item = form.save(commit=False)
#                 Resepti_item.ingredientFK = ingredient
#                 Resepti_item.save()
#                 print('ingridient ', ingredient)
#                 # return redirect('success')
#             # if category:
#             #     category_item = form.save(commit=False)
#             #     category_item.ingridientFK = category
#             #     category_item.save()
#             else:
#                 form.save()
#             return HttpResponse('successfully uploaded')
#     else:
#         form = RecipeForm()
#         form_ingridiet = IngridientForm()
#         form_category = CategoryForm()
#         context = {
#             'form': form,
#             'form_ingridiet': form_ingridiet,
#             'form_category': form_category,
#         }
        
#     return render(request, 'resepti_app/add_resepti.html', context)

