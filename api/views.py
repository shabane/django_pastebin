from django.shortcuts import render
from clipboard.models import User, Clipboard
from django.contrib.auth.hashers import check_password
from django.http import HttpResponse
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
