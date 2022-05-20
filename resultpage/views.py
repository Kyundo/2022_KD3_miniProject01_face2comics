from urllib import request
from django.shortcuts import redirect, render
from django.http import HttpResponse


def resultpage(request):
    return render(
        request, 'resultpage/result.html', {})
        