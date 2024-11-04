class User:
    name = ''
    surname = ''
    age = 0
    email = ''

    def __init__(self, name, surname, age, email):  # Конструктор
        self.name = name
        self.surname = surname
        self.age = age
        self.email = email

    def set(self, name, surname, age):  # Сеттер для изменения атрибутов
        self.name = name
        self.surname = surname
        self.age = age

# Создание объекта с помощью конструктора
user = User("John", "Doe", 30, "john.doe@example.com")

# Изменение атрибутов с помощью сеттера
user.set("Jane", "Smith", 25)

# Проверка изменений
print(user.name)      # Jane
print(user.surname)   # Smith
print(user.age)       # 25
print(user.email)     # john.doe@example.com


# Сеттеры и конструкторы — полезные инструменты для гибкой работы с объектами.
# Конструктор определяет начальное состояние, а сеттеры позволяют управлять изменениями,
# что делает код более структурированным и удобным для обновления.


# Геттеры нужны для безопасного доступа к значениям атрибутов объекта.
# Вместо прямого обращения к переменной, геттер позволяет, например,
# проверять значение, перед его использованием или возвращать его в определённом формате.

class User:
    def __init__(self, name, age):
        self.name = name
        self._age = age  # Приватная переменная

    def get_age(self):
        return f"{self._age} лет"

user = User("Иван", 30)
print(user.get_age())  # Выведет: "30 лет"

#Здесь get_age() контролирует формат возвращаемого значения.