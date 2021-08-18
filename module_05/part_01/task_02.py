from random import randint


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):

        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):

        return Point(self.x - other.x, self.y - other.y)

    def f_scalar_mul(self, scalar):

        self.x *= scalar
        self.y *= scalar

    def f_length(self):

        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __str__(self):
        return f'{self.x, self.y}'


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

print('Scalar :', sc)

p1.f_scalar_mul(sc)
p2.f_scalar_mul(sc)

print('Point 1 scalar multiplication :', str(p1))

print('Point 2 scalar multiplication :', str(p2))
