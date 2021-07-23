sum = 0

x = int(input('X:'))

while x != 0:
	sum += x % 10
	x = x // 10

print(sum)
