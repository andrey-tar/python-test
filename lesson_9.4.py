# Розробіть інтерфейс "Мережевий принтер" (NetworkPrinter),
# який включає методи для друку, сканування та копіювання.
# Потім створіть два класи: "Принтер" (Printer) та "Сканер"
# (Scanner), які реалізують цей інтерфейс та використовують
# лише ті методи, які їм потрібні. Переконайтеся, що жоден з
# класів не має пустого методу.

from abc import ABC, abstractmethod

class Printable(ABC):

    @abstractmethod
    def print_doc(self):
        pass

class Scannable(ABC):

    @abstractmethod
    def scan_doc(self):
        pass

class Copiable(ABC):

    @abstractsmethod
    def copy_doc(self):
        pass

class Printer(Printable):

    def print_doc(self):
        print("printing in progress")

class Scanner(Scannable):

    def scan_doc(self):
        print("scanning in progress")

class Network_Printer(Printable, Scannable, Copiable):

    def scan_doc(self):
        print("scanning in progress")

    def copy_doc(self):
        print("copying in progress")

    def print_doc(self):
        print("printing in progress")

print1 = Printer()
scan1 = Scanner()
net_print1 = Network_Printer()

net_print1.copy_doc()
print1.print_doc()
scan1.scan_doc()

