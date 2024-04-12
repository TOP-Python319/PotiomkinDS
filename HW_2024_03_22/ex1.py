def strong_password(password: str):
    if len(password) < 8:
        return False
    elif password.isupper() or password.islower():
        return False
    elif len(set(password) & set('1234567890')) < 2:
        print(set(password))
        return False
    elif len(set(password) & set('!@#$%^&*(_+-=[];:/<>?)')) < 1:
        return False
    else:
        return True
    
print(strong_password('aP3:kD_13'))
print(strong_password('password'))