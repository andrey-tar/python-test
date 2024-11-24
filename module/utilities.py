def calculate_average(list):
    sum = 0
    length = 0
    for num in list:
        sum += num
        length +=1
    return sum / length

def find_max(list):
    max = 0
    for num in list:
        if num >= max:
            max = num
    return max