from dataclasses import replace

# 1. Створити змінні таких типів: string, integer, float,
# bool, list, dict, tuple, None

string = 'Andrey'
integer = 5
float = 7.2
lst = [1, 3, 5]
dct = {'name':'Andrey', 'age':31}
tpl = (1, 2, 4)
print(type(string))
print(type(integer))
print(type(float))
print(type(lst))
print(type(dct))
print(type(tpl))

#2. Використати вивчені оператори та порівняти
# між собою числа, рядки, булеві значення, списки, словники і кортежі

print(string in dct)
print(integer * 5)
print(integer * float)
print(integer in lst or integer in tpl)
print(dct['age'] in tpl or dct['age'] in lst)

# Cтворити змінну num_str = 125, перевести її
# в тип string за допогою функції str()

num_str = 125
num_str = str(num_str)
print(type(num_str))

# Cтворити зміну message = 'Hi, my name is Python!'
# За допомогою функції replace() замінити
# усі букви 'y' на '0' та 'i' на '1'.

message = 'Hi, my name is Python!'
message = message.replace('y', 'o')
message = message.replace('i', '1')
print(message)

# Cтворити зміну split_test = 'This is a split test'
# і розділити її по пробілах за допомогою функції split(),
# а потім знову обʼєднати у строку за допомогою функції join()
# у змінну string_join

split_test = 'This is a split test'
split_test = split_test.split()
string_join = " ".join(split_test)
print(split_test, string_join)

# Визначити довжину рядку string_join за допомогою функції len()

print(len(string_join))

# Cтворити змінну list_append = [1, 2, 3]
# і за допомогою функції append() додати туди спочатку 4, а потім 5

list_append = [1, 2, 3]
list_append.append(4)
list_append.append(5)
print(list_append)

# Cтворити змінну list_extend = [4, 5, 6]
# і розширити цей список іншим списком [7, 8, 9]
# за допомогою функції extend()

list_extend = [4,5,6]
list_extend.extend([7,8,9])
print(list_extend)

# Визначити індекс елемента 6 у списку list_extend
# за допомогою функції index()

print(list_extend.index(6))

# Визначити довжину списку list_append за допомогою функції len()

print(len(list_append))

# Cтворити змінну dict_test = {'car': 'Toyota', 'price': 4900, 'where': 'EU'}
# та вивести на екран дані, які знаходяться в ключах car та where

dict_test = {'car':'Toyota','price':4900,'where':'EU'}
print(dict_test.get('car'),dict_test.get('where'))

# За допомогою функцій keys() і values() вивести на екран ключі та їх значення

print(dict_test.keys())
print(dict_test.values())

# За допомогою функції items() вивести на екран пари ключ - значення

print(dict_test.items())