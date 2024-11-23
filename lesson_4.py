#task 1.1
first_list = [1,2,3,4,5]
first_list.append(10)
first_list.append(20)
print(first_list)
first_list.remove(10)
print(first_list)
print()

#task 1.2
second_list = [1,2,3,4,5.9,10,929]
summ = 0
index = 0
for items in second_list:
    i = second_list[index]
    summ += i
    index +=1
print(summ)
print()

#task 1.3
third_list = [1,2,3,4,5.9,10,929]
index = 0
third_list_2=[]
for items in third_list:
    mult = third_list[index]*2
    third_list_2.append(mult)
    index +=1
print(third_list_2)
print()

#task 2.1
word_tuple = ('apple','banana','orange')
print(word_tuple[0])
print(word_tuple[1])
print(word_tuple[2])
print()

#task 2.2
tuple1 = (1,2,3)
tuple2 = (4,5,6)
tuple3 = tuple1 + tuple2
print(tuple3)

#task 3.1
sport_dict = {'name':'Sergei Rebrov',
              'age':'50',
              'sport':'football',
              'team':'Dynamo'}
print(sport_dict)
print()

#task 3.2
book_dict = {'Dark Tower':'1982',
             'Slaughterhouse-Five':'1969',
             'Ham on Rye':'1982'}
book_dict.update({"The Chronicles of Amber": '1970'})
print(book_dict)
print()

#test 3.3
cap_dict = {'Ukraine':'Kyiv',
            'Russia':'Moscow',
            'USA':'Washington'}
input = 'Moscow'
if input in cap_dict.keys():
    print(cap_dict.get(input))
else: print('Wrong country')