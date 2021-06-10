"""
Complete the method which accepts an array of integers, and returns one of the following:

"yes, ascending" - if the numbers in the array are sorted in an ascending order
"yes, descending" - if the numbers in the array are sorted in a descending order
"no" - otherwise
You can assume the array will always be valid, and there will always be one correct answer.
"""


def is_sorted_and_how(arr):
    if arr == sorted(arr):
        return 'yes, ascending'
    elif arr == sorted(arr)[::-1]:
        return 'yes, descending'
    else:
        return 'no'


if __name__ == '__main__':
    x = is_sorted_and_how([1, 3, 2, 5])
    print(f'It is sorted?: {x}')
    y = is_sorted_and_how([1, 2, 3, 4])
    print(f'It is sorted?: {y}')
    z = is_sorted_and_how([4, 3, 2, 1])
    print(f'It is sorted?: {z}')
