from django.http import response
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import HttpResponse, HttpResponseRedirect, render
from .forms import RecipeForm, CategoryForm, IngredientForm
from django.core.files.storage import FileSystemStorage


def index (request):
    print('ajskjasbd')
    return render(request, 'resepti_app/index.html')

def add_resepti(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        cat = CategoryForm(request.POST)
        #print('REQUEST:: ', form.base_fields)

        if cat.is_valid() and cat.cleaned_data['cat_name']:
            category = cat.save()
        else:
            category = None
        
        if form.is_valid():
            if category:
                Resepti_item = form.save(commit=False)
                Resepti_item.categoryFK = category
                Resepti_item.save()
                print('category ', category)
            else:
                form.save()
            return HttpResponse('successfully uploaded')
    else:
        form = RecipeForm()
        form_ingrediet = IngredientForm()
        form_category = CategoryForm()
        context = {
            'form': form,
            'form_ingridiet': form_ingrediet,
            'form_category': form_category,
        }
        
    return render(request, 'resepti_app/add_resepti.html', context)
  
  
def success(request):
    return HttpResponse('successfully uploaded2')






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

