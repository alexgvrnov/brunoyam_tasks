from random import randint

n = 5

m = [[randint(0, 100) for i in range(n)] for j in range(n)]

print(m)

mx = m[0][0]

for row in range(n):
	for elem in m[row]:
		mx = max(mx, elem)

print(mx)
