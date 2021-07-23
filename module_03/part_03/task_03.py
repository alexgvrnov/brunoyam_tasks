def num_compare(x,y):

	xf = float(x)
	yf = float(y)
	r = 0

	while (xf // 10) > 0:
		xf /= 10

	while (yf // 10) > 0:
		yf /= 10

	if xf > yf:
		r = x
	else:
		r = y

	return r
		 
def num_max(l):

	rr = 0
	rs = ''

	while len(l) > 0:

		max = l[0]
		maxx = 0

		for x in l:
			if num_compare(x,max) == x:
				max = x
		
		rs += str(max)
		l.remove(max)

	rr = int(rs)

	return rr

ll = []

n = int(input('Введите количество чисел: '))

for x in range(n):
	xx = int(input('Введите число: '))
	ll.append(xx)

res = num_max(ll)

print(res)
