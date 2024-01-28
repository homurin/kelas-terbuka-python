# anonymous function
# currying <- Haskell Curry

# regular function

def create_pow(num: float, pow: int):
    return num**pow

result = create_pow(2, 2)
print(f'regular function: {result}')

# anonymous function or currying

def curr_pow(pow: int):
    return lambda num: num**pow 

num = curr_pow(3)

print(f'with currying: {num(2)}')
print(f'with currying: {curr_pow(2)(3)}')