import sys

translation_table = {
    0: 'zero',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    5: 'five',
}

digit = int(sys.argv[1])
print(translation_table[digit])
