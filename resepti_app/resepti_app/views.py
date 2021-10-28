from django.http import response
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import HttpResponse, HttpResponseRedirect, render
from .forms import ReseptiForm, IngridientForm, CategoryForm
from django.core.files.storage import FileSystemStorage


def index (request):
    print('ajskjasbd')
    return render(request, 'resepti_app/index.html')

def add_resepti(request):
    
    if request.method == 'POST':
        form = ReseptiForm(request.POST, request.FILES)
        ing = IngridientForm(request.POST)
        cat = CategoryForm(request.POST)
        #print('REQUEST:: ', form.base_fields)

        if cat.is_valid() and cat.cleaned_data['cat_name']:
            category = cat.save()
        else:
            category = None

        if ing.is_valid() and ing.cleaned_data['ing_name']:
            ingridient = ing.save()
        else:
            ingridient = None
        
        if form.is_valid():
            if ingridient:
                Resepti_item = form.save(commit=False)
                Resepti_item.ingridientFK = ingridient
                Resepti_item.save()
                print('ingridient ', ingridient)
                # return redirect('success')
            # if category:
            #     category_item = form.save(commit=False)
            #     category_item.ingridientFK = category
            #     category_item.save()
            else:
                form.save()
            return HttpResponse('successfully uploaded')
    else:
        form = ReseptiForm()
        form_ingridiet = IngridientForm()
        form_category = CategoryForm()
        context = {
            'form': form,
            'form_ingridiet': form_ingridiet,
            'form_category': form_category,
        }
        
    return render(request, 'resepti_app/add_resepti.html', context)
  
  
def success(request):
    return HttpResponse('successfully uploaded2')



