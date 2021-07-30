def f_key_sort(x):
    xf = float(x)

    while (xf // 10) > 0:
        xf /= 10

    return xf


def num_max(l):
    l.sort(key=f_key_sort, reverse=True)

    rs = ''

    for elem in l:
        rs += str(elem)

    return int(rs)


print('Введите список чисел через пробел: ')

input_list = [int(x) for x in input().split()]

print(num_max(input_list))
