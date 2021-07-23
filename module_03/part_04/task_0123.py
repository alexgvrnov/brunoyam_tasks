import json
import os.path

def register(login, passwd):

	r = True

	usersd = {}

	with open('p.json','r') as file:
		usersd = json.load(file)

	for k in usersd.keys():
		if k == login:
			r = False

	if r:
		usersd[login] = passwd
		with open('p.json','w') as file:
			json.dump(usersd, file)

	return r

def login_function(login, passwd):

	r = False

	usersd = {}

	with open('p.json','r') as file:
		usersd = json.load(file)

	for x, y in usersd.items():
		if x == login and y == passwd:
			r = True 
	
	return r			

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
