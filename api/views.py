from django.shortcuts import render
from clipboard.models import User, Clipboard
from django.contrib.auth.hashers import check_password
from django.http import HttpResponse
from clipboard import views as utils
# Create your views here.

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


##### todo

