from abc import ABC, abstractclassmethod
import math

# task 1

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

# task 2

class Shape(ABC):

    @classmethod
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