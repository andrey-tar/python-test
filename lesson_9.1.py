# Завдання 1: Принцип єдиного обов'язку
# (Single Responsibility Principle - SRP))
#
# Спроектуйте і реалізуйте клас "Користувач" (User),
# який відповідає принципу SRP. В цьому класі повинні бути методи для створення
# користувача, оновлення даних користувача та видалення користувача.
# Переконайтеся, що кожен метод відповідає за одну конкретну функцію.

class User:

    def __init__(self, name, type):
        self.name = name
        self.type = type

    def change_user_name(self, value):
        self.name = value

    def change_user_type(self, value):
        self.type = value

    def delete_user(self):
        del self.__dict__

    def get_user_info(self):
        try:
           return f"Name: {self.name} \nPosition: {self.type}"
        except AttributeError:
            return"no user found"


user1 = User("vasya", "admin")
user2 = User("kolya", "user")

print(user1.get_user_info())
print(user2.get_user_info())
print("")

user1.change_user_name("tolik")
user2.change_user_type("zver")

print(user1.get_user_info())
print(user2.get_user_info())
print("")

user2.delete_user()

print(user1.get_user_info())
print(user2.get_user_info())
print("")
