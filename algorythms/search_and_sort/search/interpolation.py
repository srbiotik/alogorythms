# Insertion sort implementation
import sys
from random import randint


def main(ls, item):
    '''This is how we do it'''
    idx0 = 0
    idxn = len(ls) - 1
    found = False

    while ind0 <= indn and ls[ind0] <= item and ls[indn] >= item and not found:
        mid = (first + last) // 2

        if ls[mid] == item:
            found = True
        elif ls[mid] < item:
            first = mid + 1
        else:
            last = mid - 1

    return found, item, mid


if __name__ == '__main__':
    try:
        if len(sys.argv) < 2:
            raise ValueError('Not enough arguments')

        # Binary search assumes sorted input
        input_ls = sorted([int(arg) for arg in sys.argv[1:]])
        result = main(input_ls, randint(0, len(input_ls) - 1))
        print(result)

    except ValueError as e:
        print(e)
