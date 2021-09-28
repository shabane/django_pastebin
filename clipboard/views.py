from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    text = """
[Hi, this site is a online clipboard manager],
[Thease line on the head of your clipboard will help you to decide what to do],
[Click on 'file' icon to copy the text to clipboard],
[by clicking on 'trash' icon delete a text from clipboard manager],
[share a clipboard text by click on the 'share' button],
"""
    return render(request, 'index.html', {'text': text })


def new(request):
    return HttpResponse('new')


def login(request):
    return HttpResponse('login page')


def register(request):
    return HttpResponse('sing up')


def share(request):
    return HttpResponse('share')
