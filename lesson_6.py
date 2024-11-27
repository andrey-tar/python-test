# task 1
class Animal:
    name = "Nancy"
    species = "cow"
    age = 5

    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def make_sound(self):
        if hasattr(self, "sound"):
            print(getattr(self, "sound"))
        elif self.species == "cow":
            self.sound = "moooooo"
            print(getattr(self, "sound"))
        elif self.species == "cat":
            self.sound = "meow"
            print(getattr(self, "sound"))
        elif self.species == "dog":
            self.sound = "bark"
            print(getattr(self, "sound"))


animal1 = Animal("Tom", "dog", 9)
animal2 = Animal("Drew", "cat", 2)

animal2.make_sound()
animal1.make_sound()
print("")

# task 2
class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def check_values(self):
        for attr in self.__dict__:
            if getattr(self, attr, False) <= 0:
                print(f"{attr} can't be 0 or less, changing to 2")
                setattr(self, attr, 2)

    def calculate_area(self):
        self.check_values()
        self.area = self.width * self.height
        print(f"The area is {self.area}")
        delattr(self, "area")

    def get_attrs(self):
        print(self.__dict__)

rect_correct = Rectangle(12,16)
rect_wrong = Rectangle(0, -2)

rect_correct.calculate_area()
print("")
rect_wrong.calculate_area()