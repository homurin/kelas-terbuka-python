# regular function

def square_func(num: float = 0):
    return num**2


print(square_func(2))

# lambda function

square_lam = lambda num:num**2
print(square_lam(3))

# with two parameter

calculate_power = lambda num, pow : num**pow
print(calculate_power(3,3))