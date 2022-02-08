# Bubble sort implementation
import sys


def main(ls):
    '''This is how we do it'''
    for slot in range(len(ls) - 1, 0, -1):
        max_index = 0
        for i in range(1, slot + 1):
            if ls[i] > ls[max_index]:
                max_index = i

        ls[slot], ls[max_index] = ls[max_index], ls[slot]

    return ls


if __name__ == '__main__':
    try:
        if len(sys.argv) < 2:
            raise ValueError('Not enough arguments')

        result = main([int(arg) for arg in sys.argv[1:]])
        print(result)

    except ValueError as e:
        print(e)
