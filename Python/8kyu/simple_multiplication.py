"""This kata is about multiplying a given number
by eight if it is an even number and by nine otherwise."""


def simple_multiplication(number):
    if number % 2 == 0:
        return number*8
    else:
        return number*9


def simple_multiplication2(number):
    return number * 9 if number % 2 else number * 8


if __name__ == '__main__':
    x = simple_multiplication(3)
    y = simple_multiplication2(10)
    print(x, y)
