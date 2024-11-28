# Завдання 3: Принцип підстановки Лісков
# (Liskov Substitution Principle - LSP)
#
# Створіть ієрархію класів для геометричних фігур,
# де кожен підклас (наприклад, "Квадрат" і "Круг") може замінити
# базовий клас "Фігура" без порушення функціональності.
# Переконайтеся, що ці підкласи можуть використовуватися
# замість базового класу у всіх контекстах без проблем.


class Shape:

    def __init__(self, type):
        self.type = type
        self.properties = {}

    def set_properties(self, color, angles):
        self.properties = {"color": color, "angles": angles}

    def get_properties(self):
        return self.properties

class Triangle(Shape):

    def __init__(self,type):
        self.type = type
        self.properties = {}

class Rectangle(Shape):

    def __init__(self,type):
        self.type = type
        self.properties = {}

red_tri = Triangle("triangle")
red_tri.set_properties("red", 3)

blue_tri = Triangle("triangle")
blue_tri.set_properties("blue", 3)

square = Shape("square")
square.set_properties("white", 4)

red_rect = Rectangle("rectangle")
red_rect.set_properties("red", 4)

white_rect = Rectangle("rectangle")
white_rect.set_properties("white", 4)

colors = [red_tri, blue_tri, square, red_rect, white_rect]

def get_concr_color_shape(color):
    count = 0
    mark_type = []
    for shape in colors:
        if shape.properties["color"] == color:
            count +=1
            mark_type.append(shape.type)
    print(f"Count of color: {count}\ntypes: {mark_type}")

get_concr_color_shape("red")