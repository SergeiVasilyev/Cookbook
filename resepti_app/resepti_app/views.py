from django.http import response
from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse, HttpResponseRedirect, render
from .forms import RecipeForm, CategoryForm, IngredientForm
from django.core.files.storage import FileSystemStorage
from .models import Recipe, Ingredient, Category
from django.db.models import Q


def index (request):
    recipes = Recipe.objects.all()
    context = {
        'recipes': recipes,
    }  
    return render(request, 'resepti_app/index.html', context)

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
                form.save()
                print('category ', category)
            else:
                form.save()
            # elem = Recipe.objects.get(categoryFK=category)
            return redirect('add_resepti')
            # return redirect('/resepti/' + str(elem))
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

def resepti(request, idx):
    recipe = Recipe.objects.get(id=idx)
    context = {
        'recipe': recipe,
    }
    return render(request, 'resepti_app/resepti.html', context) 

def search(request):  
    if request.method == 'GET':
        print('search_form: ', request.GET.get('search_form'))
        request_form = request.GET.get('search_form')
        items = Ingredient.objects.filter(ing_name__icontains=request_form)
        category_items = Category.objects.filter(cat_name__icontains=request_form)
        body_text_items = Recipe.objects.filter(body_text__icontains=request_form)
        headline_items = Recipe.objects.filter(headline__icontains=request_form)
        if not items.exists() and not body_text_items.exists() and not headline_items.exists() and not category_items.exists():
            recipes = None
            print('recipes ', None)
        else:
            recipes = Recipe.objects.filter(Q(ingredients__in=items) | Q(body_text__icontains=request_form) | Q(headline__icontains=request_form) | Q(categoryFK__in=category_items)).distinct()
            print('recipes ', recipes)
    context = {
        'recipes': recipes,
    }
    return render(request, 'resepti_app/index.html', context)


def edit_resepti(request, id):
    data_item = Recipe.objects.get(id=id)

    form = RecipeForm(instance=data_item)
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=data_item)
        if form.is_valid():
            form.save()
            return redirect('/resepti/' + str(id))
    context = {
        'form': form,
    }
    return render(request, 'resepti_app/edit_resepti.html', context)
    # return HttpResponse('successfully uploaded: ' + str(id))

def poista_resepti (request, idx):
    item = Recipe.objects.get(id=idx)
    item.delete()
    return redirect ('home')