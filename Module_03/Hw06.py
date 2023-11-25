def format_string(string, length):
    if len(string) >= length:
        return string
    else:
        c = ' '
        return f'{c * ((length - len(string)) // 2)}{string}'

print(format_string(length = 15, string='abaa'))