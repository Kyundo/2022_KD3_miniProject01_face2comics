from urllib import request
from django.shortcuts import redirect, render
<<<<<<< HEAD
from django.http import HttpResponse
from config import settings
import os
from .models import UploadFile


=======
from django.http import HttpResponse, JsonResponse
>>>>>>> d8d386a17692e349c831714aeba2a63404e7630f

def homepage(request):
    return render(
        request, 'homepage/main.html', {})

def index(request):
    return render(
        request, 'homepage/index.html', {})
        
def gallery(request):
    return render(
        request, 'homepage/gallery.html', {})
        
def contact(request):
    return render(
        request, 'homepage/contact.html', {})
<<<<<<< HEAD
=======
        
def index1(request):
    return render(
        request, 'homepage/index1.html', {})
>>>>>>> d8d386a17692e349c831714aeba2a63404e7630f


def test(request):
    if request.method == 'POST':
        upload_file = request.FILES.get('file') # 파일 객체
        name = upload_file.name # 파일 이름
        size = upload_file.size # 파일 크기
<<<<<<< HEAD
        with open(name, 'wb') as file: # 파일 저장
            for chunk in upload_file.chunks():
                file.write(chunk)
        return HttpResponse('%s<br>%s' % (name, size))
    return render(request, 'homepage/upload1.html')

def upload2(request):
    if request.method == 'POST':
        upload_files = request.FILES.getlist('file')
        result = ''
        for upload_file in upload_files:
            name = upload_file.name
            size = upload_file.size
            with open(name, 'wb') as file:
                for chunk in upload_file.chunks():
                    file.write(chunk)
            result += '%s<br>%s<hr>' % (name, size)
        return HttpResponse(result)
    return render(request, 'homepage/upload2.html')

from .forms import UploadFileForm
def upload3(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploadFile = form.save()
# uploadFile = form.save(commit=False)
            name = uploadFile.file.name
            size = uploadFile.file.size
            return HttpResponse('%s<br>%s' % (name, size))
    else:
        form = UploadFileForm()
    return render(
        request, 'homepage/upload3.html', {'form': form})

def download(request):
    id = request.GET.get('id')
    #uploadFile = UploadFile.objects.get(id=id)
    uploadFile = UploadFile.objects.order_by('-id')[0]

    filepath = str(settings.BASE_DIR) + ('/image/%s' % uploadFile.file.name)
    #filepath = 'C:\\Users\\admin\\django\\example/%s' % uploadFile.file.name

    filename = os.path.basename(filepath)
    with open(filepath, 'rb') as f:
        response = HttpResponse(f, content_type='application/octet-stream')
        response['Content-Disposition'] = 'attachment; filename=%s' % filename
        return response        

=======
<<<<<<< HEAD
        with open(name, 'wb') as file: # 파일 저장
            for chunk in upload_file.chunks():
                file.write(chunk)
=======
    with open(name, 'wb') as file: # 파일 저장
        for chunk in upload_file.chunks():
            file.write(chunk)
>>>>>>> e4554fe5de3e53c5aef54d7b2d3cfdfdce4a799a
        return HttpResponse('%s<br>%s' % (name, size))
    return render(request, 'homepage/test.html')

def upload(request):
    if request.method == 'POST':
        upload_file = request.FILES.get('files') # 파일 객체
        name = upload_file.name # 파일 이름
        size = upload_file.size # 파일 크기
        print(name, size)
        with open('static/photo/%s' % name, 'wb') as file: # 파일 저장
            for chunk in upload_file.chunks():
                file.write(chunk)

        context = {
            'data': {
                'length': 1
            }
        }

        return JsonResponse(context)
>>>>>>> d8d386a17692e349c831714aeba2a63404e7630f
