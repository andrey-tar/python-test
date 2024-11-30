# Створіть Python-файл з ім'ям `calculator.py`. У цьому файлі
# створіть наступні функції:
#
# 1. `add(a, b)`: Приймає два числа `a` і `b` та повертає їхню суму.
# 2. `subtract(a, b)`: Приймає два числа `a` і `b` та повертає їхню різницю.
# 3. `multiply(a, b)`: Приймає два числа `a` і `b` та повертає їхній добуток.
# 4. `divide(a, b)`: Приймає два числа `a` і `b` і повертає результат ділення
#   `a` на `b`. Пам'ятайте про можливість ділення на нуль і додайте
#   перевірку цього варіанту.
#
#  Після створення цих функцій, напишіть програму, яка імпортує модуль
# `calculator.py` і використовує його функції для виконання обчислень.
# Попросіть користувача ввести два числа і операцію (додавання, віднімання,
# множення або ділення), і виведіть результат обчислення.

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