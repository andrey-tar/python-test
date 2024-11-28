# Напишіть програму, яка встановлює початковий пароль
# і перевіряє, чи введений користувачем пароль співпадає
# з ним. Якщо пароль дорівнює "password123", виведіть повідомлення
# "Ви увійшли в систему". В іншому випадку
# виведіть повідомлення "Неправильний пароль".

password = 'password123'
input_field = input("Enter password:")
if input_field == password:
    print('You entered the system')
else: print('Wrong password')
print()

# Створіть програму, яка встановлює номер дня тижня і виводить назву
# відповідного дня тижня. Якщо номер дня недійсний (менше 1
# або більше 7), виведіть повідомлення про помилку.

week_list = ["monday", 'tuesday', 'wednesday', 'thursday','friday','saturday','sunday']
input_day = int(input("Choose day number (1-7):"))

if input_day <1 or input_day >7:
    print("there's something wrong")
else: print(week_list[input_day], "is a day of the week #", input_day)
print()

# Виведіть таблицю множення для заданого числа від 1 до 10.
num = int(input("Multiplication table for number:"))
multip = 1

while multip <= 10:
    print(num, " * ", multip, " = ", num * multip)
    multip +=1
print()

# Визначте список чисел і обчисліть їх суму.

sum_list = [12,15,13,19]
summ = 0

for num in sum_list:
    summ = summ + num
print (summ)
print()

# Обчисліть факторіал заданого числа.

target = int(input("Factorial for number:"))
num = 1
factor = 1
while num <= target:
    factor = factor * num
    num +=1
print (f"factorial of {target} is", factor)
print()

#Виведіть всі парні числа від 1 до 50.

start = 1
end = 50
lst = []

while start <= end:
    check_1 = start / 2
    check_2 = start // 2
    float(check_2)
    if check_1 == check_2:
        lst.append(start)
        start +=1
    else: start +=1
print(lst)
print()

# Знайдіть всі прості числа в заданому діапазоні.

start_2 = int(input("Range start for simple numbers:"))
end_2 = int(input("Range end for simple numbers:"))
while start_2 >= end_2:
    end_2 = int(input(f"Number should be bigger than {start_2}:"))

lst = []

for i in range(start_2,end_2+1):
    for j in range(2,i):
        if i % j == 0:
            break
    else: lst.append(i)
print(lst)