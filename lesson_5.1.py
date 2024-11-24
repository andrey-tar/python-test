from module import calculator

list_of_oper = ('*','+','-','/')
while True:
    try:
        a = int(input("select first number: "))
        break
    except ValueError:
        print("No valid number, try again...")
while True:
    try:
        b = int(input("select second number: "))
        break
    except ValueError:
        print("No valid number, try again...")
operation = input("choose operation: + - * /: ")
while operation not in list_of_oper:
    try:
        print("No valid operator, try again...")
        operation = input("choose correct operation: + - * /: ")
    except : pass
if "+" in operation:
    print(f"{a} + {b} = {calculator.add(a, b)}")
elif "-" in operation:
    print(f"{a} - {b} = {calculator.subtract(a, b)}")
elif "*" in operation:
    print(f"{a} * {b} = {calculator.multiply(a, b)}")
elif "/" in operation:
    if b == 0:
        print("You can't divide by 0")
    else: print(f"{a} / {b} = {calculator.divide(a, b)}")