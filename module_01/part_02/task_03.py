p_correct = False
while p_correct == False:
	p = input("Введите пароль:")
	if len(p) > 8:
		p_sl = False
		p_su = False
		for symbol in p:
			if symbol.islower():
				p_sl = True
			if symbol.isupper():
				p_su = True
		if p_sl and p_su:
			p_correct = True
			print("Пароль введен корректно")
		else:
			print("Пароль должен содержать заглавные и строчные символы")	
	else:
		print("Пароль не больше 8 символов")
