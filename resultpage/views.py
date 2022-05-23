from urllib import request
from django.shortcuts import redirect, render
from django.http import HttpResponse


def resultpage(request):
    id = request.GET.get('id')
    imgs = ['닥터스트레인지', '로키', '블랙위도우', '블랙팬서', '비전', '스칼렛위치', '스타로드', '스파이더맨', '아이언맨', '앤트맨', '캡틴마블', '캡틴아메리카', '타노스', '토르', '헐크', '호크아이',]
    texts = ['닥터스트레인지', '로키', '블랙위도우', '블랙팬서', '비전', '스칼렛위치', '스타로드', '스파이더맨', '아이언맨', '앤트맨', '캡틴마블', '캡틴아메리카', '타노스', '토르', '헐크', '호크아이',]

    file_name = imgs[int(id)]
    hero_story = texts[int(id)]

    return render(
        request, 'resultpage/result.html', 
        {'file_name': file_name}, 
        {'hero_story': hero_story},)
        