message = input("Enter a message: ")
offset = int(input("Enter the offset: "))
encoded_message = ""
for ch in message:
    if 0 <= ord(ch) - ord('a') < 26:
        encoded_message += chr((ord(ch) - ord('a') + offset) % 26 + ord('a'))
    elif 0 <= ord(ch) - ord('A') < 26:
        encoded_message += chr((ord(ch) - ord('A') + offset) % 26 + ord('A'))
    else: 
        encoded_message += ch      