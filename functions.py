def printAll(*params):
    for i in params:
        print(i * 2)
    print('\n')


printAll(45, 25, 'Hello', 23.5)
printAll(25, 85)


def printDict(**args):
    for key, value in args.items():
        print("Ключ:", key, ", значение:", value)


printDict(long="Vasiliy", short="Vasya", on=True)
print('\n')

mult = lambda a, x=23: a * x  # анонимная функция

print(mult(2))
print(mult(3, 14))

mult = lambda *args: print(args)

mult(2, "String", False)
mult(3, 5)
