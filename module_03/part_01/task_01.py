x = float(input('X:'))
p = float(input('P:'))
y = float(input('Y:'))

while y > x:
	x += x * p / 100
	x = ((x * 100) // 1) / 100
	print(x)
	print('---')
print('X больше или равно Y')	
