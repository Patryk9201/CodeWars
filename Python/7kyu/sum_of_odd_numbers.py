"""Given the triangle of consecutive odd numbers:

             1
          3     5
       7     9    11
   13    15    17    19
21    23    25    27    29
"""


def row_sum_odd_numbers(n):
    return n**3


if __name__ == '__main__':
    x = row_sum_odd_numbers(15)
    print(x)
