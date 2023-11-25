first = int(input("Enter the first integer: "))
second = int(input("Enter the second integer: "))

gcd = first if first < second else second 
while True:
    if first % gcd == 0 and second % gcd == 0:
        break
    gcd -= 1
    