from random import randint

n = 23

l_num = [randint(0, 100) for i in range(n)]

print(l_num)

l_num.sort()

print(l_num)

number = int(input('Введите число для поиска: '))

not_found = True

min_num = 0
max_num = n


while not_found:

    current = min_num + int((max_num-min_num) / 2)

    print(min_num, max_num, current)

    if l_num[current] == number:
        print('Число найдено, позиция в списке = ', current)
        not_found = False

    if (current == min_num) and not_found:
        print('Число не найдено')
        not_found = False

    if l_num[current] > number:
        max_num = current
    else:
        min_num = current
