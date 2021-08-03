from random import randint

n = 23

l_num = [randint(0, 100) for i in range(n)]


def bin_search(l_number, number):

    not_found = True

    min_num = 0
    max_num = len(l_number)

    position = 0

    while not_found:

        position = min_num + int((max_num-min_num) / 2)

        if l_number[position] == number:
            not_found = False

        if (position == min_num) and not_found:
            position = -1
            not_found = False

        if l_number[position] > number:
            max_num = position
        else:
            min_num = position

    return position


l_num.sort()

print(l_num)

num = int(input('Введите число для поиска: '))

result = bin_search(l_num, num)

if result != -1:
    print('Число найдено, позиция в списке:', result)
else:
    print('Число не найдено')
