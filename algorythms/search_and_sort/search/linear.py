# Insertion sort implementation
import sys
from random import randint


def main(ls, item):
    '''This is how we do it'''
    index = 0
    found = False

    while index < len(ls) and not found:
        if ls[index] == item:
            found = True
        else:
            index += 1

    return found


if __name__ == '__main__':
    try:
        if len(sys.argv) < 2:
            raise ValueError('Not enough arguments')

        input_ls = [int(arg) for arg in sys.argv[1:]]
        main(input_ls, randint(0, len(input_ls) - 1))

    except ValueError as e:
        print(e)
