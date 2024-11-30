# Створіть власний Python-модуль з ім'ям `utilities.py`. У цьому модулі
# створіть наступні функції:
#
# 1. `calculate_average(numbers)`: Приймає список чисел `numbers` і
#   повертає середнє арифметичне цих чисел.
# 2. `find_max(numbers)`: Приймає список чисел `numbers` і повертає
#   найбільше число у списку.
#
# Після створення цього модуля, створіть інший Python-файл
# (наприклад, `main.py`), який імпортує модуль `utilities.py` і
# використовує його функції для обробки списку чисел.
#
# В `main.py` створіть список чисел та використовуйте функції
# з модуля `utilities` для знаходження середнього значення та
# найбільшого числа у списку. Виведіть результати на екран.

from module import utilities

list_num = [1,24,43,15,16,2,7,8]

print(f"The average of the list if {utilities.calculate_average(list_num)}")
print(f"The max number on the list is {utilities.find_max(list_num)}")