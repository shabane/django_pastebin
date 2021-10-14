from django.http.response import JsonResponse
from django.shortcuts import render
import clipboard
from clipboard.models import User, Clipboard
from django.contrib.auth.hashers import check_password
from django.http import HttpResponse
from clipboard import views as utils
from hashlib import blake2b

def AddText(request):
    user = request.GET['user']
    password = request.GET['password']
    text = request.GET['text']
    user = User.objects.filter(username=user)
    if(user):
        if(check_password(password, user[0].password)):
            Clipboard.objects.create(author=user[0], text=text)
            return HttpResponse('text added') # temp response
        else:
            print('incorrect username or password')
    else:
        print('incorrect username or password')


def UserLogin(request):
    user = request.GET['user']
    password = request.GET['password']
    user = User.objects.filter(username=user)
    if(user):
        if(check_password(password, user[0].password)):
            return HttpResponse('username and password is correct') # temp
        else:
            return HttpResponse('username or password incorrect')
    else:
        return HttpResponse('username or password incorrect')


def DeleteText(request):
    user = request.GET['user']
    password = request.GET['password']
    textId = request.GET['id']
    user = User.objects.filter(username=user)
    if(user):
        if(check_password(password, user[0].password)):
            if(Clipboard.objects.filter(id=textId, author=user[0]).delete()[0] == 1):
                return HttpResponse('object deleted') # temp
            else:
                return HttpResponse('object not found')
        else:
            return HttpResponse('username or password incorrect')
    else:
        return HttpResponse('username or password incorrect')


def ShareText(request):
    user = request.GET['user']
    password = request.GET['password']
    textId = request.GET['id']
    user = User.objects.filter(username=user)
    if(user):
        if(check_password(password, user[0].password)):
            clipb = Clipboard.objects.filter(pk=textId, author=user[0])
            if(clipb):
                if(not clipb[0].link):
                    link = blake2b(clipb[0].text.encode('utf-8'), digest_size=3).hexdigest()
                    clipb.update(link=link)
                    return HttpResponse('link created') # temp
                else:
                    return HttpResponse('link created')
            else:
                return HttpResponse('object not found')
        else:
            return HttpResponse('username or password incorrect')
    else:
        return HttpResponse('username or password incorrect')


def CheckChanges(request):
    user = request.GET['user']
    password = request.GET['password']
    user = User.objects.filter(username=user)
    if(user):
        if(check_password(password, user[0].password)):
            texts_id = []
            for i in Clipboard.objects.filter(author=user[0]):
                texts_id.append(i.id)
            return JsonResponse({'TextsId': texts_id})
        else:
            return JsonResponse({
                'result': False,
                'msg': 'username or password incorrect'
            })
    else:
        return JsonResponse({
                'result': False,
                'msg': 'username or password incorrect'
            })