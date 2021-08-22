from random import randint


class Point:

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def __add__(self, other):

        return Point(self.__x + other.__x, self.__y + other.__y)

    def __sub__(self, other):

        return Point(self.__x - other.__x, self.__y - other.__y)

    def __mul__(self, other):

        x = 0
        y = 0

        if type(other) == int:

            x = self.__x * other
            y = self.__y * other

        else:

            raise TypeError('Multiplication is possible only with scalar (int type)')

        return Point(x, y)

    def f_length(self):

        return (self.__x ** 2 + self.__y ** 2) ** 0.5

    def __str__(self):

        return f'{self.__x, self.__y}'


def main_task():

    p1 = Point(randint(-10, 10), randint(-10, 10))
    p2 = Point(randint(-10, 10), randint(-10, 10))

    print('Point 1: ', str(p1))
    print('Point 2: ', str(p2))

    p3 = p1 + p2

    print('Sum: ', str(p3))

    p3 = p1 - p2

    print('Sub : ', str(p3))

    print('Length 1: ', p1.f_length())
    print('Length 2: ', p2.f_length())

    sc = randint(2, 10)

    print('Scalar for Point 1 :', sc)

    try:
        p1 *= sc
    except TypeError:
        print('Multiplication is possible only with scalar (int type)')

    print(str(p1))

    sc = 'trend to follow'

    print('Scalar for Point 2:', sc)

    try:
        p2 *= sc
    except TypeError:
        print('Multiplication is possible only with scalar (int type)')

    print(str(p2))


main_task()
