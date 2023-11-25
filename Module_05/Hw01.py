def real_len(text):
    symbols = ['\n', '\f', '\r', '\t', '\v']
    length = 0
    for i in range(len(text)):
        if text[i:i+1] in symbols:
            i += 1
        else: 
            length += 1
    return length


print(real_len('Alex\nKdfe23\t\f\v.\r'))
