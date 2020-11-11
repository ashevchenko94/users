
account1 = {'login' : 'ivan', 'password' : 'q1'}
account2 = {'login' : 'petr', 'password' : 'q2'}
account3 = {'login' : 'olga', 'password' : 'q3'}
account4 = {'login' : 'anna', 'password' : 'q4'}

user1 = {'name' : 'Иван', 'age' : 20, 'account' : account1}
user2 = {'name' : 'Петр', 'age' : 25, 'account' : account2}
user3 = {'name' : 'Ольга', 'age' : 18, 'account' : account3}
user4 = {'name' : 'Анна', 'age' : 27, 'account' : account4}


user_list = [user1, user2, user3, user4]
account_list = [account1, account2, account3, account4]

#запрашиваем ключ
first_task = input("Введите ключ (name или account): ").lower()

try:
    print(f"значение ключа {first_task} для юзера 1 = {user1[first_task]}")
    print(f"значение ключа {first_task} для юзера 2 = {user2[first_task]}")
    print(f"значение ключа {first_task} для юзера 3 = {user3[first_task]}")
    print(f"значение ключа {first_task} для юзера 4 = {user4[first_task]}")
except:
    print("Введенный ключ не найден")

#Выдаем информацию по запрашиваемому пользователю
user = int(input("Введите порядковый номер: ")) - 1

try:
    print(f"Данные по юзеру № {user}: \n"
    f"Имя: {user_list[user]['name']} \n"
    f"Возраст: {user_list[user]['age']} \n"
    f"Аккаунт: {account_list[user]['login']} \n"
    f"Пароль: {account_list[user]['password']}")
except:
    print('Пользователь с указанным номером не найден')

#Перемещение пользователя
user_move = int(input("Введите номер пользователя, которого нужно переместить в конец: ")) - 1

#Выводим пользователя которого нужно переместить в конец
print(user_list[user_move])
#Первоначальный спислк
print(user_list)

#Формируем новый список
removed_user = user_list.pop(user_move)
user_list.append(removed_user)
print(user_list)

#Выводим средний возраст
total_ages = 0

for i in user_list:
    age = i.get('age')
    total_ages += age

avarage_age = total_ages/len(user_list)    
    
print(f'Средний возраст юзеров {avarage_age}')