import random


def minmax(numbers):
    """
    ########################################
    Code Your Program here
    ########################################
    """

    ########################################
    # Do not delete the return statement
    ########################################
    return maxval, minval


def main():

    numbers = [1, 2, 3, 4, 5]
    maxval, minval = minmax(numbers)
    print('List values', *numbers)
    print(f'Max value: {maxval} \t Min value:{minval}')

    numbers = [random.randint(0, 100) for i in range(10)]
    maxval, minval = minmax(numbers)
    print('List values', *numbers)
    print(f'Max value: {maxval} \t Min value: {minval}')


if __name__ == '__main__':
    main()
