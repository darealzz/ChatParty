from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth

# Create your views here.

def index(request):
    if request.user.is_authenticated == True: #If they are logged in, send them to the home page. Else to the login page.
        return redirect('/home')
    else:
        return redirect('/login')

def home(request):

    ctx = {'Title': 'Home'}
    return render(request, 'home.html', ctx)

def login(request):

    ctx = {'Title': 'Login'}
    return render(request, 'login.html', ctx)
