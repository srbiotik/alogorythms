# Bubble sort implementation
import sys


def main(input):
    '''This is how we do it'''
    last_element_index = len(input) - 1
    for i in range(last_element_index):
        prev = i - 1
        curr = i
        while input[prev] > input[curr] and prev >= 0:
            input[prev], input[curr] = input[curr], input[prev]
            curr, prev = prev, prev - 1

    print(input)
    return(input)


if __name__ == '__main__':
    try:
        if len(sys.argv) < 2:
            raise ValueError('Not enough arguments')

        main([int(arg) for arg in sys.argv[1:]])

    except ValueError as e:
        print(e)
