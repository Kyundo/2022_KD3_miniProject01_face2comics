from urllib import request
from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse


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
        
def index1(request):
    return render(
        request, 'homepage/index1.html', {})


def test(request):
    if request.method == 'POST':
        upload_file = request.FILES.get('file') # 파일 객체
        name = upload_file.name # 파일 이름
        size = upload_file.size # 파일 크기
        with open(name, 'wb') as file: # 파일 저장
            for chunk in upload_file.chunks():
                file.write(chunk)
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
