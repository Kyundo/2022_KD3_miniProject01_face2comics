from urllib import request
from django.shortcuts import redirect, render
from django.http import HttpResponse


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
        

def upload1(request):
    if request.method == 'POST':
        upload_file = request.FILES.get('file') # 파일 객체
        name = upload_file.name # 파일 이름
        size = upload_file.size # 파일 크기
    with open(name, 'wb') as file: # 파일 저장
        for chunk in upload_file.chunks():
        file.write(chunk)
        return HttpResponse('%s<br>%s' % (name, size))
    return render(request, 'file/upload1.html')