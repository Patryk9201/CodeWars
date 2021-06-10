"""Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.

The output should be two capital letters with a dot separating them.

It should look like this:

Sam Harris => S.H

Patrick Feeney => P.F"""


def abbrev_name(name):
    return '.'.join(w[0] for w in name.split()).upper()


if __name__ == '__main__':
    x = abbrev_name("Sam Harris")
    print(f'Sam Harris => {x}')
    y = abbrev_name("Patrick Feeney")
    print(f'Patrick Feeney => {y}')
