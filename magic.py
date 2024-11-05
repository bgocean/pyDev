#  print(dir(int))

# num = 10
# print(num + 7)

class Some:
    def __add__(self, str):
        print("Some" + str)

    def __new__(self):
       self.__add__(self, "new")
       self.__init__(self) 

    def __init__(self):
        print("Init started")    

obj = Some()
# obj + "new"
print(dir(obj))