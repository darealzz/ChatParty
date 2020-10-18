from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate as authenticate_user
from django.contrib.auth import login as auth_login
from django.contrib import messages
from .utilities import Utilities

# Create your views here.

def index(request):
    if request.user.is_authenticated == True: #If they are logged in, send them to the home page. Else to the authenticate page.
        return redirect('/home')
    else:
        return redirect('/authenticate')

def home(request):
    if request.user.is_authenticated == True: #If they are logged in, send them to the home page. Else to the authenticate page.
        pass
    else:
        return redirect('/authenticate')


    ctx = {'Title': 'Home'}
    return render(request, 'home.html', ctx)

def authenticate(request):
    if request.user.is_authenticated == True: #If they are logged in, send them to the home page. Else to the authenticate page.
        return redirect('/home')
    else:
        pass

       
    if request.method == 'POST':
        if 'login' in request.POST:
            username = request.POST['Username']
            password = request.POST['Password']

            if not username or not password:
                messages.add_message(request, messages.INFO, 'Looks like you forgot to fill out a field or two!', extra_tags='login oops')
                return redirect('/')

            user = authenticate_user(request, username=username, password=password)
            if user:
                auth_login(request, user)
                return redirect('/home/')
            elif not user:
                messages.add_message(request, messages.INFO, 'It seems that you have given me some invalid data :(', extra_tags='login')
                return redirect('/')

        elif 'signup' in request.POST:
            email = request.POST['Email']
            username = request.POST['Username']  
            password = request.POST['Password']
            confirm_password = request.POST['Confirm_Password']         
            
            email_validate = Utilities.validate_email(email)
            username_validate = ''
            password_validate = Utilities.validate_password(password, confirm_password)

            if not email or not username or not password or not confirm_password:
                messages.add_message(request, messages.INFO, f'Looks like you forgot to fill out a field or two!', extra_tags='signup')

            elif email_validate != True:
                messages.add_message(request, messages.INFO, f'{email_validate}', extra_tags='signup')

            elif password_validate != True:
                messages.add_message(request, messages.INFO, f'{password_validate}', extra_tags='signup')
                

            ctx = {'Title': 'Authenticate', 'Tab': 'signup'}
            return render(request, 'authenticate.html', ctx)

    else:
        ctx = {'Title': 'Authenticate'}
        return render(request, 'authenticate.html', ctx)


# class Message_Send(CreateView): 
#     #TODO 

# class Message_Detail(CreateView): 
#     #TODO 

# class MessageBox(ListView): 

