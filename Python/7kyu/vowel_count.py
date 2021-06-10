"""Return the number (count) of vowels in the given string.

We will consider a, e, i, o, u as vowels for this Kata (but not y).

The input string will only consist of lower case letters and/or spaces."""


def get_count(s):
    return sum(c in 'aeiou' for c in s)


if __name__ == '__main__':
    x = get_count("abracadabra")
    print(x)
