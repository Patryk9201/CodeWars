"""
You are given two interior angles (in degrees) of a triangle.
Write a function to return the 3rd.
Note: only positive integers will be tested.
"""


def other_angle(a, b):
    if a + b > 180 or not 0 < a < 180 or not 0 < b < 180:
        return "ERROR"
    return 180 - a - b


if __name__ == '__main__':
    x = other_angle(100, 20)
    print(x)
