class Utilities:
# Checking email #    
    def validate_email(email): 
        email = str(email)
        if '@' not in email:
            return 'Please provide a real email.'
            
        email_lst = email.split('@')
        if len(email_lst) != 3: # ['Example', '@', 'example.com'], false for ['Ex', '@', 'mple', '@', 'example.com']
            return 'Please provide a real email.'

        if '.' not in email_lst[2]: # 'example.com'
            return 'Please provide a real email.'

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
    def validate_password(password, second): 
        password = str(password) 
        special_chars = """¬`!"£%^&*()_-+={[}]:;@'~#?/>.<,"""
        specials = 0
        upper = 0
        lower = 0
        nums = 0

        if password != second:
            return 'Seems like your passwords dont match...'

        for char in password:
            if char.upper() == char:
                upper += 1
            if char.lower() == char:
                lower += 1
            if char in special_chars:
                specials += 1
            try:
                if isinstance(int(char), int) == True:
                    nums += 1
            except:
                continue

        if specials + upper + lower + nums >= 4:
            return True
        else:
            return 'Your password must contain a Special Character, an upper and lowercase character, and a number.'
            

        
