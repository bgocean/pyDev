import pickle

# user = {'name': 'John', 'age': 34, 'weight': 87}
# file = open('user.pickle', "wb")
# pickle.dump(user, file)
# file.close()

user = {'name': 'John', 'age': 34, 'weight': 87}

# # Открываем файл в режиме записи бинарных данных
# with open('user.pickle', 'wb') as file:
#     pickle.dump(user, file)

# with open('user.pickle', 'rb') as file:
#     loaded_user = pickle.load(file)
#     print(loaded_user)


file_in = open('user.pickle', "rb")
user_new = pickle.load(file_in)
file_in.close()

print(user_new)
print(user_new['age'])