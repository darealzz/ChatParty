from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib import messages

# Create your views here.

def index(request):
    if request.user.is_authenticated == True: #If they are logged in, send them to the home page. Else to the login page.
        return redirect('/home')
    else:
        return redirect('/login')

def home(request):
    if request.user.is_authenticated == True: #If they are logged in, send them to the home page. Else to the login page.
        pass
    else:
        return redirect('/login')


    ctx = {'Title': 'Home'}
    return render(request, 'home.html', ctx)

def login(request):
    if request.user.is_authenticated == True: #If they are logged in, send them to the home page. Else to the login page.
        return redirect('/home')
    else:
        pass


    if request.method == 'POST':
        username = request.POST['Username']
        password = request.POST['Password']

        user = authenticate(request, username=username, password=password)
        if user:
            auth_login(request, user)
            return redirect('/home/')
        else:
            print(User.objects.get(username=username))
            return redirect('/') 

    else:
        ctx = {'Title': 'Login'}
        return render(request, 'login.html', ctx)

