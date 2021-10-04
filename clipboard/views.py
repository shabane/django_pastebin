from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse, request
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


def delete(request):
    if(request.user.is_authenticated):
        if(request.method == 'GET'):
            id = request.GET['id']
            if(id.isdigit()):
                if(Clipboard.objects.filter(id=id)):
                    Clipboard.objects.get(pk=id).delete()
                    return HttpResponseRedirect('/')
                else:
                    result = """
                        'result': False,
                        'msg': 'object not fount'
                    """
                    return HttpResponse(result)
    else:
        return HttpResponse('you dont have <b>permisson</b> to do this')