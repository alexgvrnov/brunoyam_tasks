import json
import os.path


def register(login, passwd):
	not_registered = True

	with open('p.json', 'r') as file:
		users_d = json.load(file)

	for k in users_d.keys():
		if k == login:
			not_registered = False

	if not_registered:
		users_d[login] = passwd
		with open('p.json','w') as file:
			json.dump(users_d, file)

	return not_registered


def login_function(login, passwd):
	registered = False

	with open('p.json','r') as file:
		users_d = json.load(file)

	for x, y in users_d.items():
		if x == login and y == passwd:
			registered = True
	
	return registered


usersinit = {'admin': 'admin'}

if os.path.exists('p.json'):
	print('Файл паролей существует')
else:
	with open('p.json','w') as file:
		json.dump(usersinit, file)
		print('Файл паролей создан')

choice = int(input('Введите 1 для регистрации или 2 для входа в систему :'))

login = input('Введите логин: ')
passwd = input('Введите пароль: ')

if choice == 1:
	if register(login, passwd):
		print('Пользователь добавлен')
	else:
		print('Пользователь уже существует')
elif choice == 2:
	if login_function(login, passwd):
		print('Успешный вход')
	else:
		print('Логин или пароль неверные')
else:
	print('Ошибка выбора')
