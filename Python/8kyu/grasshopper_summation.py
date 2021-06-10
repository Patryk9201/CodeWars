"""
Write a program that finds the summation of every number from 1 to num.
The number will always be a positive integer greater than 0.
For example:
summation(2) -> 3
1 + 2
summation(8) -> 36
1 + 2 + 3 + 4 + 5 + 6 + 7 + 8
"""


def summation(num):
    return (1+num) * num / 2


if __name__ == '__main__':
    x = summation(10)
    print(f'sum of your numbers: {x}')
