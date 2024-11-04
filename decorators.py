def auth(func):  # Декоратор
    def wrapper():
        isAuth = True  # Если будет False, то show() не выполнится
        if (isAuth):
            func()
        else:
            print("Ypu need to be auth")
    return wrapper


def test(func):
    def wrapper():
        print("Text before function")
        func()
        print("Text after function")
    return wrapper

@test
@auth
def show():
    print("Show function")


@auth
def index():
    print("Index function")


@auth
def about():
    print("About function")


show()
# index()
# about()
