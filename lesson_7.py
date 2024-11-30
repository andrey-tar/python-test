# Створіть базовий клас `Vehicle` (транспортний засіб), який містить
# наступні атрибути:
#
# - `make` (виробник)
# - `model` (модель)
# - `year` (рік виробництва)
#
# Додайте конструктор класу `Vehicle`, який ініціалізує ці атрибути.
#
# Створіть підкласи (похідні класи) від `Vehicle` для різних видів
# транспорту, наприклад, `Car`, `Motorcycle`, `Bicycle`, тощо. Кожен
# підклас повинен мати додаткові атрибути та методи, які є специфічними
# для цього виду транспорту. Наприклад, для класу `Car` можна додати
# атрибут `fuel_type` та метод `start_engine()`.
#
# Створіть об'єкти для кожного з підкласів та виведіть їхні атрибути
# на екран.
#
# Створіть метод `display_info()` у базовому класі `Vehicle`, який
# виводить загальну інформацію про транспортний засіб (наприклад,
# "Це [виробник] [модель] [рік] року виробництва.").
#
# В кожному з підкласів перевизначте метод `display_info()` для
# виведення специфічної інформації про цей вид транспорту.
#
# Створіть список об'єктів з різних видів транспорту, викличте метод
# `display_info()` для кожного об'єкта, і спостерігайте за тим, як
# поліморфізм дозволяє викликати правильну версію методу для кожного
# об'єкта


class Vehicle:
    """Base class"""

    def __init__(self, make, model, year) -> None:
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"This is {self.make} {self.model} {self.year} of production")


class Car(Vehicle):
    """Class for cars"""

    def __init__(self, make, model, year, fuel_type) -> None:
        super().__init__(make, model, year)
        self.fuel_type = fuel_type

    def start_engine(self):
        print(self.__dict__)
        print("")
        print(f"Oh, you're driving {self.make} {self.model}?")
        print(f"don't forget to get some {self.fuel_type}")

    def display_info(self):
        print(f"This is {self.make} {self.model} {self.year} of production, and it's a car")



class Bicycle(Vehicle):
    """Class for bicycles"""

    def __init__(self, make, model, year, number_of_wheels) -> None:
        super().__init__(make, model, year)
        self.number_of_wheels = number_of_wheels

    def spin_the_wheels(self):
        print(self.__dict__)
        print("")
        print(f"Spin your {self.number_of_wheels}-wheeler faster!")

    def display_info(self):
        print(f"This is {self.make} {self.model} {self.year} of production, and it's a bicycle")

car1 = Car("Honda","Civic", "2000", "gas")
bicycle1 = Bicycle("Romet", "Mountain", "2020",2)

bicycle1.spin_the_wheels()
print("")
car1.start_engine()
print("")
bicycle1.display_info()
print("")
car1.display_info()