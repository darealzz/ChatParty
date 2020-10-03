from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages


def register(request):

    if request.method == 'POST':
        First_Name = request.POST['First_Name']
        Last_Name = request.POST['Last_Name']
        Email = request.POST['Email']
        Username = request.POST['Username']
        Password = request.POST['Password']
        Confirm_Password = request.POST['Confirm_Password']

        if Password == Confirm_Password:
            if User.objects.filter(username=Username).exists() == True:
                messages.info(request, 'Username Taken.')
                return redirect('register')

            elif User.objects.filter(email=Email).exists() == True:
                messages.info(request, 'Email is already registered.')
                return redirect('register')
            else:
                user = User.objects.create_user(username=Username, password=Password, email=Email, first_name=First_Name, last_name=Last_Name)
                user.save()
                return redirect('/account')

        else:
            messages.info(request, 'Passwords do not match.')
            return redirect('register')

    else:
        return render(request, 'register.html', {'PageName': 'Register'})


def login(request):
    if request.method == 'POST':
        Username = request.POST['Username']
        Password = request.POST['Password']

        user = auth.authenticate(username=Username, password=Password)
        if user: #If credentials match
            auth.login(request, user)
            return redirect('/account')
        else:
            messages.info(request, 'Invalid Credentials.')
            return redirect('login')

    else:
        return render(request, 'login.html', {'PageName': 'Login'})

def profile(request):
    return render(request, 'profile.html', {'PageName': 'Profile'})

