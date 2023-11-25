result = None
operand = None
operator = None
wait_for_number = True
operator_list = "+-/*"

while True:
    if wait_for_number:
        operand = input()
        try:
            operand = int(operand)
            if operator == "+":
                result += operand
            elif operator == "-":
                result -= operand
            elif operator == "*":
                result *= operand
            elif operator == "/":
                result /= operand
            else:
                result = operand
            wait_for_number = False
        except ValueError:
            print(f"{operand} is not a number. Try again.")
    if not wait_for_number:
        operator = input()
        if operator == "=":
            print (result)
            break
        if not operator in operator_list:
            print(f"{operator} is not '+' or '-' or '/' or '*'. Try again.")
        else:
            wait_for_number = True