#task 1.1
password = 'password123'

if password == "password123":
    print('You entered the system')
else: print('Wrong password')
print()

#task 1.2
week_list = ["monday", 'tuesday', 'wednesday', 'thursday','friday','saturday','sunday']
day_num = 1

if day_num <1 or day_num >7:
    print("there's something wrong")
else: print(week_list[day_num], "is a day of the week #", day_num)
print()

#task 2.1
num = 6
multip = 1

while multip <= 10:
    print(num, " * ", multip, " = ", num * multip)
    multip +=1
print()

#test 2.2
sum_list = [12,15,13,19]
summ = 0

for num in sum_list:
    summ = summ + num
print (summ)
print()

#test 2.3
target = 9
num = 1
factor = 1
while num <= target:
    factor = factor * num
    num +=1
print (f"factorial of {target} is", factor)
print()

#test 2.4
start = 1
end = 50

while start <= end:
    check_1 = start / 2
    check_2 = start // 2
    float(check_2)
    if check_1 == check_2:
        print(start)
        start +=1
    else: start +=1
print()

#test 2.5
start_2 = 6
end_2 = 2000
lst = []

for i in range(start_2,end_2+1):
    for j in range(2,i):
        if i % j == 0:
            break
    else: lst.append(i)
print(lst)