from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def index(request):

    colors = [
        '#335c67;',
        '#01957d',
        '#536c69',
        '#172e1a',
        '#4ac75',
        '#8c432a',
        '#610094',
    ]

    text = """
[Hi, this site is a online clipboard manager],
[Thease line on the head of your clipboard will help you to decide what to do],
[Click on 'file' icon to copy the text to clipboard],
[by clicking on 'trash' icon delete a text from clipboard manager],
[share a clipboard text by click on the 'share' button],
"""

    return render(request, 'index.html', 
    {
        'text': text,
        'qcolor': colors[random.randint(0, len(colors)-1)]
    })


def new(request):
    return HttpResponse('new')


def login(request):
    return HttpResponse('login page')


def register(request):
    return HttpResponse('sing up')


def share(request):
    return HttpResponse('share')
