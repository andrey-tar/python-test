from calendar import error

import requests

site = "https://jsonplaceholder.typicode.com"

# Створіть Python-сценарій, який використовує бібліотеку
# requests для виконання GET-запиту до веб-ресурсу та виведення
# вмісту веб-сторінки на екран. Використовуйте функцію
# requests.get() для виконання запиту.

# Розширте попереднє завдання, додаючи можливість вказати параметри
# запиту. Виконайте GET-запит до веб-ресурсу, передаючи параметри
# запиту, такі як параметри запиту у URL або параметри через словник.

placeholder_types = ["/posts", "/comments", "/albums", "/photos", "/todos", "/users"]
user_input = input(f"Choose webpage from {placeholder_types}")
while user_input not in placeholder_types:
    user_input = input(f"Choose from the following list: {placeholder_types}\n")

response_get = requests.get(url=site + user_input)
print(response_get.text)
print("---------------------------")

# Створіть Python-сценарій для виконання POST-запиту до веб-ресурсу.
# Відправте дані на сервер, наприклад, форму з ім'ям користувача і паролем.

# Після виконання запиту, розпарсьте вміст HTTP-відповіді та виведіть
# потрібну інформацію. Наприклад, виведіть заголовки відповіді або
# вміст сторінки.

body = {
    "userId": 69,
    "password": "password_qwerty123"
}
response_post = requests.post(url=site + "/users", data=body)
print(response_post.status_code)
print(response_post.reason)
print(response_post.text)
print("-----------------------------")

# Розширте ваш код, щоб зберегти отриманий вміст веб-сторінки у файл.
# Використайте функціонал Python для роботи з файлами для збереження вмісту.

f = open("lesson_10 export.txt", "w")
f.write(response_post.text)