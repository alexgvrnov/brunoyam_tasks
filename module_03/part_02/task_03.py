d = {1: 10 , 2: 20 , 3: 30}
dd = {}

for k, v in d.items():
	dd[v] = k

print(d)

d.clear()
d.update(dd)

print(d)
