count = 1
password = input("Введите пароль:")
login = input('Введите логин:')
while count < 3:
    if password == '123456' and login == 'gg11':
        print('Успешно')
        break
    else:
        count += 1
        password = input("Введите пароль:")
        login = input('Введите логин:')

