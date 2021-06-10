"""
When provided with a number between 0-9, return it in words.

Input :: 1

Output :: "One".
"""


def switch_it_up(number):
    switch = {
            0: "Zero",
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine",
            }
    if 0 <= number <= 9:
        return switch[number]


def switch_it_up2(number):
    return ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"][number]


if __name__ == '__main__':
    x = switch_it_up(0)
    y = switch_it_up2(3)
    print(x, y)
