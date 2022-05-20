from urllib import request
from django.shortcuts import redirect, render
from django.http import HttpResponse


def homepage(request):
    return render(
        request, 'homepage/main.html', {})
        