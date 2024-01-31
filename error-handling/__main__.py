# simple example

# input = int(input('first num: '))


# try:
#     result = 10 / input
#     print(result)
# except:
#     print('input cannot be zero')

# apps example

from numbers import Number
while True:
    a = int(input('input first num: '))
    b = int(input('input first num: '))

    try:
        result = a / b
        print(f'result: {result}')
        is_done = str(input('continue? [Y/n]'))
        if (is_done.lower() == 'n'):
            break
    except:
        print('input number cannot be zero')

print('exit from program')

# create exception


def add(a: int, b: int) -> int:
    if not isinstance(a, Number) or isinstance(b, Number):
        raise 'input must be a integer!'
    return a+b

# get error message


a = 0

try:
    x = 10 / a
    print(x)
except Exception as err_message:
    print(err_message)

# get error type

try:
    x = 10 / "0"
except ZeroDivisionError as err_message:
    print(err_message)
except TypeError as err_message:
    print(err_message)
