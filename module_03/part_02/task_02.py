from random import randint

n = 5

m = [[randint(0,100) for i in range(n)] for j in range(n)]

print(m)

max = 0

for x in range(n):
	for y in m[x]:
		if y > max:
			max = y
print(max)			
