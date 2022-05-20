from urllib import request
from django.shortcuts import redirect, render
from django.http import HttpResponse


def quiz(request):
    return render(
        request, 'quiz/quiz.html', {})
        
