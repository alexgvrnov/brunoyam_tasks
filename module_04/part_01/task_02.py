from random import randint

n = 23

l_num = [randint(0, 100) for i in range(n)]

print(l_num)


def f_item_positioning(l_update, position):

    if l_update[position - 1] > l_update[position]:

        l_update.insert(position - 1, l_update.pop(position))

        if position != 1:

            f_item_positioning(l_update, position - 1)

    pass


for x in range(1, n):

    f_item_positioning(l_num, x)

    print('')
    print('Шаг:', x)
    print(l_num)
