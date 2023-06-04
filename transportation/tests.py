from django.test import TestCase

# Create your tests here.


def x_change_mem(x):

    x.extend(list(range(1, 100000)))


x = [1, 2]

print(id(x))

x_change_mem(x)

print(id(x))

if __name__ == '__main__':
    pass

