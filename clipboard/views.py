from typing import Text
from django import http
from django.http.response import Http404, HttpResponseForbidden, HttpResponseNotAllowed, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse, request, JsonResponse
import random
from .models import Clipboard
from hashlib import blake2b

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
                "مدیریت آنلاین کلیپ برد",
            ]
    return render(request, 'per/index.html', 
    {
        'text': text,
        'qcolor': colors[random.randint(0, len(colors)-1)]
    })


def logout(request):
    return render(request, 'per/logout.html', {})


def support(request):
    return render(request, 'support.html', {})


def guide(request):
    return render(request, 'per/guide.html', {})


def delete(request):
    if(request.user.is_authenticated):
        if(request.method == 'GET'):
            id = request.GET['id']
            if(id.isdigit()):
                if(Clipboard.objects.filter(id=id, author=request.user)):
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


def share(request):
    if(request.user.is_authenticated):
        if(request.method == 'GET'):
            id = request.GET['id']
            if(id.isdigit()):
                if(Clipboard.objects.filter(pk=id, author=request.user)):
                    clipb = Clipboard.objects.get(pk=id)
                    link = blake2b(clipb.text.encode('utf-8'), digest_size=3).hexdigest()
                    Clipboard.objects.filter(pk=id).update(link=link)
                    return HttpResponseRedirect('/')
                else:
                    result = {
                        'result': False,
                        'msg': 'object not found'
                    }
                    return HttpResponse(result)
            else:
                result = """
                    'result': False,
                    'msg', 'you should pass a digit as id'
                """
                return HttpResponse(result)
    else:
        result = """
            'result', False,
            'msg', 'you dont have permision to do this, pleas log in fist'
        """
        return HttpResponse(result)


def shared(request, link):
    colors = [
        '#FF6F61;',
        '#6B5B95',
        '#009B77',
        '#DD4124',
        '#45B8AC',
        '#EFC050',
        '#7FCDCD',
    ]

    text = Clipboard.objects.filter(link=link)
    if(text):
        text = text[0]
    else:
        return HttpResponseNotFound('404 not found')
        
    print(text)
    context = {
        'qcolor': colors[random.randint(0, len(colors)-1)],
        'text': text
    }
    return render(request, 'per/shared.html', context)


def search(request):
    if(request.user.is_authenticated):
        if(request.method == 'GET'):
            colors = [
                '#FF6F61;',
                '#6B5B95',
                '#009B77',
                '#DD4124',
                '#45B8AC',
                '#EFC050',
                '#7FCDCD',
            ]

            user = request.user
            q = request.GET['text']
            text = Clipboard.objects.filter(text__icontains=q, author=user).order_by('-id')
            visiblity = 'visible'
            if(not text):
                text = ['nothing matches :(']
                visiblity = 'hidden'

            context = {
                'qcolor': colors[random.randint(0, len(colors)-1)],
                'text': text,
                'visiblity' : visiblity,
                'searched': q
            }
            return render(request, 'per/search.html', context)
    else:
        result = """
            login first <a href='/accounts/login'>login</a>
        """
        return HttpResponse(result)


def add(request):
    if(request.user.is_authenticated):
        if(request.method == 'POST'):    
            text = request.POST['text']
            if(len(text.strip())):
                Clipboard.objects.create(text=text, author=request.user)
                return HttpResponseRedirect('/')
    else:
        return HttpResponse('please login first <a href="/accounts/login">login</a>')
    return render(request, 'per/add.html', {})

