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
    
    text = Clipboard.objects.filter(author=request.user).order_by('-id')
    
    return render(request, 'index.html', 
    {
        'text': text,
        'qcolor': colors[random.randint(0, len(colors)-1)]
    })



