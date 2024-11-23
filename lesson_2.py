from dataclasses import replace

#task 1.1
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

#task 1.2
print(string in dct)
print(integer * 5)
print(integer * float)
print(integer in lst or integer in tpl)
print(dct['age'] in tpl or dct['age'] in lst)

#task 2.1
num_str = 125
num_str = str(num_str)
print(type(num_str))

#task 2.2
message = 'Hi, my name is Python!'
message = message.replace('y', 'o')
message = message.replace('i', '1')
print(message)

#task 2.3
split_test = 'This is a split test'
split_test = split_test.split()
string_join = " ".join(split_test)
print(split_test, string_join)

#task 2.4
print(len(string_join))

#task 3.1
list_append = [1, 2, 3]
list_append.append(4)
list_append.append(5)
print(list_append)

#task 3.2
list_extend = [4,5,6]
list_extend.extend([7,8,9])
print(list_extend)

#task 3.3
print(list_extend.index(6))

#task 3.4
print(len(list_append))

#task 4.1
dict_test = {'car':'Toyota','price':4900,'where':'EU'}
print(dict_test.get('car'),dict_test.get('where'))

#task 4.2
print(dict_test.keys())
print(dict_test.values())

#task 4.3
print(dict_test.items())