sm = 0

x = int(input('X:'))

while x != 0:
	sm += x % 10
	x //= 10

print(sm)
