# Bubble sort implementation
import sys


def main(ls):
    '''This is how we do it'''
    distance = len(ls) // 2
    while distance > 0:
        for i in range(distance, len(ls)):
            j = i
            temp = ls[i]

            while j >= distance and ls[j - distance] > temp:
                ls[j] = ls[j - distance]
                j = j - distance
            ls[j] = temp
        distance //= 2

    return ls


if __name__ == '__main__':
    try:
        if len(sys.argv) < 2:
            raise ValueError('Not enough arguments')

        result = main([int(arg) for arg in sys.argv[1:]])
        print(result)

    except ValueError as e:
        print(e)
