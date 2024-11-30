from abc import ABC
import math

# Створіть клас "Користувач" (User), який має такі приватні
# поля (інкапсульовані дані):
#
# - Ім'я (name)
# - Електронна пошта (email)
# - Пароль (password)

# Напишіть публічні методи для установки і отримання значень
# цих полів (геттери і сеттери). Потім створіть об'єкт класу
# "Користувач" і встановіть значення полів, а також виведіть їх
# на екран.

class User:

    def __init__(self, name, email, password):
        self.__name = name
        self.__email = email
        self.__password = password

    def set_user_name(self, value):
        self.__name = value

    def set_user_email(self, value):
        self.__email = value

    def set_user_password(self, value):
        self.__password = value

    def get_user_data(self):
        print(self.__dict__)

user = User("tom","123@gmail.com", "qwerty")

print(user.__dict__)
user.set_user_name("bob")
user.set_user_email("234@i.ua")
user.set_user_password('adsfs')
user.get_user_data()
print("")

# Створіть клас "Фігура" (Shape), який буде абстрактним класом.
# У цьому класі визначіть абстрактний метод "обчислити_площу"
# (calculate_area).
#
# Створіть підкласи цього класу для різних геометричних фігур,
# наприклад, "Коло" (Circle), "Прямокутник" (Rectangle) і "Трикутник"
# (Triangle). У кожному з підкласів реалізуйте метод "обчислити_площу"
# відповідно до формули для обчислення площі кожної фігури.
#
# Створіть об'єкти кожного з підкласів і використайте метод
# "обчислити_площу", щоб вивести площу кожної фігури на екран.

class Shape(ABC):

    @abstractmethod
    def calculate_area(self):
        pass

class Triangle(Shape):

    def __init__(self, a, h):
        self.a = a
        self.h = h

    def calculate_area(self):
        print(f"Triangle's area is {self.a * self.h / 2}")

class Rectangle(Shape):

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calculate_area(self):
        print(f"Rectangle's area is {self.a * self.b}")

class Circle(Shape):

    def __init__(self, r):
        self.r = r

    def calculate_area(self):
        self.area = round(math.pi * (self.r ** 2), 2)
        print(f"Circle's area is {self.area}")
        delattr(self, "area")

circle = Circle(8)
triangle = Triangle(5,6)
rectangle = Rectangle(4,5)

circle.calculate_area()
triangle.calculate_area()
rectangle.calculate_area()