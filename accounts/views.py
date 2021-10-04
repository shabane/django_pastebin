from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from .models import User
import re


## check the data come from post
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
def check_form(username, password1, password2, email):
    if(not User.objects.filter(username=username)):
        if(username.find(' ') == -1):
            if(len(username) >= 4 and len(username) <= 12):
                if(len(password1) >= 8):
                    if(password1 == password2):
                        if(re.fullmatch(regex, email)):
                            if(User.objects.filter(email=email)):
                                return HttpResponse('email exist')
                            else:
                                return True
                        else:
                            return HttpResponse('email is invalid')
                    else:
                        return HttpResponse('password not match')
                else:
                    return HttpResponse('password most be at least 8 character')
            else:
                return HttpResponse('username must be at least 4 character and less or equal to 12')
        else:
            return HttpResponse('username should not contain space')
    else:
        return HttpResponse('username exist, pleas choose another username')

def singup(request):
    if(request.method == 'POST'):
        form = request.POST
        form_ok = check_form(form['username'], form['password'], form['repassword'], form['email'])
        if(form_ok != True):
            return form_ok
        else:
            User.objects.create_user(form['username'].lower(), form['email'], form['password'])
            return HttpResponseRedirect('/accounts/login')
    else:
        return render(request, 'singup.html', {})