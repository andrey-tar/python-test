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