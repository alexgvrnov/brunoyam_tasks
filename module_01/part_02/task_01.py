x = int(input("Введите число X:"))
y = int(input("Введите число Y:"))
z = int(input("Введите число Z:"))
r = (x == y) + (x == z) + (y == z)
if r == 1:
	print(2)
else:
	print(r)