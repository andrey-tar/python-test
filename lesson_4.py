# Створіть список чисел. Додайте до списку числа 10 і 20,
# видаліть число 10 і виведіть отриманий список.

first_list = [1,2,3,4,5]
first_list.append(10)
first_list.append(20)
print(first_list)
first_list.remove(10)
print(first_list)
print()

# Створіть список чисел. Знайдіть та виведіть суму всіх чисел у списку.

second_list = [1,2,3,4,5.9,10,929]
summ = 0
index = 0
for items in second_list:
    i = second_list[index]
    summ += i
    index +=1
print(summ)
print()

# Створіть список чисел. Подвойте кожне число у списку та виведіть результат.

third_list = [1,2,3,4,5.9,10,929]
index = 0
third_list_2=[]
for items in third_list:
    mult = third_list[index]*2
    third_list_2.append(mult)
    index +=1
print(third_list_2)
print()

# Створіть кортеж з трьох різних предметів, таких як
# ("яблуко", "банан", "апельсин"). Виведіть кожен елемент
# кортежу окремо.

word_tuple = ('apple','banana','orange')
print(word_tuple[0])
print(word_tuple[1])
print(word_tuple[2])
print()

# Створіть два кортежі з числами і об'єднайте їх у новий кортеж.
# Виведіть отриманий кортеж.

tuple1 = (1,2,3)
tuple2 = (4,5,6)
tuple3 = tuple1 + tuple2
print(tuple3)

# Створіть словник, що містить інформацію про вашого
# улюбленого спортсмена (ім'я, вік, спорт, команда тощо).
# Виведіть цю інформацію на екран.

sport_dict = {'name':'Sergei Rebrov',
              'age':'50',
              'sport':'football',
              'team':'Dynamo'}
print(sport_dict)
print()

# Створіть словник, що містить ваші улюблені книги
# (назва книги та рік видання). Додайте до словника
# нову улюблену книгу та виведіть оновлений словник.

book_dict = {'Dark Tower':'1982',
             'Slaughterhouse-Five':'1969',
             'Ham on Rye':'1982'}
book_dict.update({"The Chronicles of Amber": '1970'})
print(book_dict)
print()

# Створіть словник, що містить інформацію про країни та
# їх столиці. Запитайте користувача про назву країни і
# виведіть столицю цієї країни (якщо така країна є у словнику).

cap_dict = {'Ukraine':'Kyiv',
            'Russia':'Moscow',
            'USA':'Washington'}
input = 'Moscow'
if input in cap_dict.keys():
    print(cap_dict.get(input))
else: print('Wrong country')