l = []
ll = []

n = int(input('Количество элементов списка N:'))

for x in range(n):
	c = input('Введите элемент списка:')
	l.append(c)

for s in l:
	if (l.count(s)) > 1 and ll.count(s) != 1:
		ll.append(s)
		
print(l)
print(ll)		
