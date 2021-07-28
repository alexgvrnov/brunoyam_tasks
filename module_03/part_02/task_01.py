duplicates = []

print('Введите элементы списка через пробел:')

input_list = [int(x) for x in input().split()]

for elem in input_list:
	if elem not in duplicates and input_list.count(elem) > 1:
		duplicates.append(elem)
		
print(input_list)
print(duplicates)
