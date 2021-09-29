from django.shortcuts import render
from django.http import HttpResponse
import random
from .models import Clipboard
# Create your views here.

def index(request):

    colors = [
        '#FF6F61;',
        '#6B5B95',
        '#009B77',
        '#DD4124',
        '#45B8AC',
        '#EFC050',
        '#7FCDCD',
    ]
    
    if(request.user.is_authenticated):
        text = Clipboard.objects.filter(author=request.user).order_by('-id')
    else:
            text = [
                "online clipboard manager. to use, just log in",
                """About me:
                im Arya Shabane programer of this site, im a software student in Isfehan Sorush Uni.
                """
            ]
    return render(request, 'index.html', 
    {
        'text': text,
        'qcolor': colors[random.randint(0, len(colors)-1)]
    })


def logout(request):
    return render(request, 'logout.html', {})

def support(request):
    return render(request, 'support.html', {})