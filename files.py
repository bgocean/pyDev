str = input("Введите текст: ")
str += '\n'

file = open('data/text.txt', 'a')  #дозапись файла
file.write(str)
file.close()


try:
    file = open('data/text.txt', 'rt')  #чтение файла в текстовом режиме (по умолчанию без r и t)
    print(file.read(10)) #прочитать 10 символов
    for line in file:
        print(line)
    file.close()
except FileNotFoundError:
    print("Файл не найден!")

