# Завдання 2: Принцип відкритості/закритості
# (Open/Closed Principle - OCP)
#
# Створіть інтерфейс "Фігура" (Shape) та два класи, які реалізують
# цей інтерфейс, наприклад, "Коло" (Circle) та "Прямокутник" (Rectangle).
# Потім додайте новий клас, який розраховує площу будь-якої фігури,
# не модифікуючи існуючі класи.
# Використовуйте принцип OCP для розширення функціональності.

from abc import ABC
import math

class Shape(ABC):

    @classmethod
    def get_area(self):
        pass

    @classmethod
    def get_perimeter(self):
        pass

class RectangleCalc(Shape):

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_area(self):
        return self.a * self.b

    def get_perimeter(self):
        return 2 * (self.a + self.b)

class CircleCalc(Shape):

    def __init__(self, r):
        self.r = r

    def get_area(self):
        return round(math.pi * (self.r ** 2), 2)

    def get_perimeter(self):
        return round(2*math.pi*self.r, 2)

class SquareCalc(Shape):

    def __init__(self, a):
        self.a = a

    def get_perimeter(self):
        return self.a * 4

    def get_area(self):
        return self.a ** 2

square = SquareCalc(6)
circle = CircleCalc(4)
rectangle = RectangleCalc(4,7)

print(square.get_area())
print(square.get_perimeter())
print(circle.get_area())
print(circle.get_perimeter())
print(rectangle.get_area())
print(rectangle.get_perimeter())