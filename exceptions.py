user_input_a = False

while user_input_a == False:
    try:

        a = int(input("Введите первое значение: "))
        user_input_a = True
    except ValueError:
        print("Введите именно ЧИСЛО!")


user_input_b = False

while user_input_b == False:
    try:
        b = int(input("Введите второе значение: "))
        user_input_b = True
    except ValueError:
        print("Введите именно ЧИСЛО!")

print("Результат: ", a + b)
