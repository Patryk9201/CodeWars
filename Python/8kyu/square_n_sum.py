"""Complete the square sum function so that it squares each number passed into it and then sums the results together.

For example, for [1, 2, 2] it should return 9 because 1^2 + 2^2 + 2^2 = 9."""


def square_sum(numbers):
    result = []
    for sqr in numbers:
        result.append(sqr ** 2)
    return sum(result)


def square_sum2(numbers):
    return sum(n ** 2 for n in numbers)


if __name__ == '__main__':
    x = square_sum([1, 2, 4])
    y = square_sum2([3, 6, 7])
    print(x, y)
