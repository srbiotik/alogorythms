# Bubble sort implementation
import sys


def main(input):
    '''This is how we do it'''
    if len(input) > 1:

        mid = len(input) // 2
        left = input[:mid]
        right = input[mid:]

        main(left)
        main(right)

        a = 0
        b = 0
        c = 0

        while a < len(left) and b < len(right):
            if left[a] < right[b]:
                input[c] = left[a]
                a += 1
            else:
                input[c] = right[b]
                b += 1

            c += 1

        while a < len(left):
            input[c] = left[a]
            a += 1
            c += 1

        while b < len(right):
            input[c] = right[b]
            b += 1
            c += 1
    return input


if __name__ == '__main__':
    try:
        if len(sys.argv) < 2:
            raise ValueError('Not enough arguments')

        result = main([int(arg) for arg in sys.argv[1:]])
        print(result)

    except ValueError as e:
        print(e)
