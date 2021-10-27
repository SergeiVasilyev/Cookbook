from django.http import response
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import HttpResponse, HttpResponseRedirect
from .forms import ReseptiForm

def index (request):
    print('ajskjasbd')
    return render(request, 'resepti_app/index.html')

def add_resepti(request):
    form = ReseptiForm()
    context = {
        'form': form
    }
    return render(request, 'resepti_app/add_resepti.html', context)








# from django.shortcuts import  render
# from django.core.files.storage import FileSystemStorage

# def upload(request):
#     if request.method == 'POST' and request.FILES['upload']:
#         upload = request.FILES['upload']
#         fss = FileSystemStorage()
#         file = fss.save(upload.name, upload)
#         file_url = fss.url(file)
#         return render(request, 'main/upload.html', {'file_url': file_url})
#     return render(request, 'main/upload.html')