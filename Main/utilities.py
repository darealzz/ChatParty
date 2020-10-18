from django.shortcuts import render, redirect
from django.contrib.auth.models import User, aut
from django.contrib.auth import authenticate, login
from requests import request 

class Utilities:
<<<<<<< HEAD
# Checking email #    
    def validate_email(email): 
        email = str(email)
        if '@' not in email:
            return False
            
        email_lst = email.split('@')
        if len(email_lst) != 3: # ['Example', '@', 'example.com'], false for ['Ex', '@', 'mple', '@', 'example.com']
            return False

        if '.' not in email_lst[2]: # 'example.com'
            return False

        return True

# Checking username #
    def check_username(username):  
        username = str(username) 
        allowed_chars = '._abcdefghjkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ23456789'
        notallowed_chars = """!"#$%&/()=?*|€÷×ßŁ}§{@{}§<>'"""
    
        for char in username: 
            if char in notallowed_chars: 
                return False 
            elif char in allowed_chars: 
                continue
            return True

# Checking email #
    def check_password(password): 
        password = str(password) 
        allowed_chars = '._abcdefghjkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ23456789!"#$%&/()=?*|€÷×ßŁ}§{@{}§<>'
        not_allowed = ''

        for char in password:
            if char in allowed_chars: 
                return True:
            elif char in not_allowed: 
                return False   

        
=======
>>>>>>> 2e7ed6479762850abb69c18104f25fc23aabe174
