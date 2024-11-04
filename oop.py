from tkinter.font import names


class User:
    name = ''
    surname = ''
    age = 0
    email = ''

    def __init__(self, name, surname, age, email):     #Конструктор __init__
        self.name = name
        self.surname = surname
        self.age = age
        self.email = email


    def set(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def print_all(self):
        print('Пользователь:', self.name, ', его возраст:', self.age, ', его мыло:', self.email)


admin = User('Admin', "Pupkin", 21, 'admin@supersite.xyz')
# admin.set('Admin', 'Pupkin', 21)
# admin.name = 'Admin'
# admin.age = 21
# admin.email = 'admin@supersite.xyz'
# print(admin.name)
admin.print_all()

bob = User('Bob', 'Marley', 30, 'bob@boberman.bo')
# bob.set('Bob', 'Marley', 30)
# bob.name = 'Bob'
# print(bob.name)
bob.print_all()