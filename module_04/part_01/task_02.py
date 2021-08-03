from random import randint

n = 23

l_num = [randint(0, 100) for i in range(n)]


def f_item_positioning(l_update, position):

    if l_update[position - 1] > l_update[position]:

        l_update.insert(position - 1, l_update.pop(position))

        if position != 1:

            f_item_positioning(l_update, position - 1)


def insertion_sort(l_upd):

    for x in range(1, len(l_upd)):

        f_item_positioning(l_upd, x)


print(l_num)

insertion_sort(l_num)

print(l_num)
