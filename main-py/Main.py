# __main__ = top level code env

# __name__ == __main__
# will happen at main file program

import some_lib
print(f'__name__ {__name__}')

# __name__ at external program


# declaration


def add(a: int, b: int) -> int:
    return int(a+b)

# main function


if __name__ == '__main__':
    print(f'results: {add(1, 2)}')
