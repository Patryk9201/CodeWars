"""Task:

Given a list of integers, determine whether the sum of its elements is odd or even.

Give your answer as a string matching "odd" or "even".

If the input array is empty consider it as: [0] (array with a zero)."""


def odd_or_even(arr):
    return 'even' if sum(arr) % 2 == 0 else 'odd'


if __name__ == '__main__':
    x = odd_or_even([2, 5, 5])
    print(x)
