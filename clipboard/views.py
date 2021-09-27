from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    text = """
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
"""
    text = str(text)
    return render(request, 'index.html', {'text': text })


def new(request):
    return HttpResponse('new')


def login(request):
    return HttpResponse('login page')


def register(request):
    return HttpResponse('sing up')


def share(request):
    return HttpResponse('share')
