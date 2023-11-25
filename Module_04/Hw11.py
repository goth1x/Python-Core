def is_valid_password(password):
    if len(password) != 8 or password.upper() == password or password.lower() == password:
        return False
    for i in password:
        if i.isdigit():
            return True
    return False


print(is_valid_password('S|7QY(Cb'))
