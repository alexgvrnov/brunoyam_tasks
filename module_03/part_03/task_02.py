s = '''Было просто пасмурно, дуло с севера
А к обеду насчитал сто градаций серого.
Так всегда первого ноль девятого
То ли весь мир сошел с ума, то ли я - того...
На столе записка от нее смятая
Недопитый виски допиваю с матами.
Посмотрю в окно, допишу главу
Первое сентября, дворник жжет листву.
Серым облакам наплевать на нас
Если знаешь как жить - живи
Ты хотела плыть как все - так плыви!'''


def f_make_word(s):

	sl = [',', '.', '!', '-']

	for c in sl:
		s = s.replace(c, '')

	return s


def f_make_word_2(word):
	exeptions = (',', '.', '!', '-')

	while word.startswith(exeptions):
		word = word[1:]

	while word.endswith(exeptions):
		word = word[:-1]

	return word


def f_list_less_5(l):

	rl = []

	words = l.split()

	for word in words:
		correct_word = f_make_word_2(word)
		if len(correct_word) < 5 and correct_word != '':
			rl.append(correct_word)

	return rl


print(s)
print(f_list_less_5(s))
