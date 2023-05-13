# Insertion sort implementation
import sys


def main(input):
    '''This is how we do it'''
    for j in range(len(input) - 1, 0, -1):
        for i in range(j):
            if input[i] > input[i + 1]:
                input[i + 1], input[i] = input[i], input[i + 1]

    print(input)
    return(input)


if __name__ == '__main__':
    try:
        if len(sys.argv) < 2:
            raise ValueError('Not enough arguments')

        main([int(arg) for arg in sys.argv[1:]])

    except ValueError as e:
        print(e)
