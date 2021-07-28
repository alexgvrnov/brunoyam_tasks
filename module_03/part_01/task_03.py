summa = 0

x = int(input('X:'))

while x != 0:
	summa += x % 10
	x //= 10

print(summa)
