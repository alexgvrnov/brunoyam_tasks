def f_area(a, b, c):

	p = (a + b + c) / 2

	s = (p * (p - a) * (p - b) * (p - c)) ** 0.5

	return s

a = float(input('Введите сторону A: '))
b = float(input('Введите сторону B: '))
c = float(input('Введите сторону C: '))

r = f_area(a, b, c)

print(r)
