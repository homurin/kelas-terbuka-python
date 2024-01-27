import os


def rectangle_perimeter(length: float = 0, width: float = 0):
    return 2 * (length + width)


def rectangle_area(length: float = 0, width: float = 0):
    return length * width


while True:
    os.system('clear')
    print(f"{'PROGRAM TO CALCULATE':^40}")
    print(f"{'PERIMETER AND AREA OF A RECTANGLE':^40}")
    print(f"{'='*40:^40}")

    LENGTH = float(input('input length: '))
    WIDTH = float(input('input width: '))
    PERIMETER = rectangle_perimeter(LENGTH, WIDTH)
    AREA = rectangle_area(LENGTH, WIDTH)
    print(f"{'='*40:^40}")
    print(f'rectangle perimeter: {PERIMETER}')
    print(f'rectangle area: {AREA}')

    is_done = input('exit program [Y/n]')

    if (is_done == 'n'):
        continue
    else:
        break
