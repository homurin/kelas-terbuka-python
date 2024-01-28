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

# reason to user lambda

# wihout lambda

admiral = ['aokiji', 'kizaru', 'akainu', 'fujitora', 'ryokugyu']

# sort by name

admiral.sort()
print(admiral)

# sort by name length

admiral.sort(key=len)

print(admiral)

# alternative way

def name_len(name):
    return len(name)

admiral.sort(key=name_len)
print(admiral)

# using lambda

shicibukai = ['chrocodile', 'mihawk', 'doflamingo', 'moria', 'kuma', 'boa', 'jinbei']
shicibukai.sort(key=lambda name: len(name))

print(shicibukai)

# filter

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def lower_than_five(num: list[int]):
    return num < 5

new_num = list(filter(lower_than_five, num))

print(new_num)

lambd_num = list(filter(lambda x:x <= 5, num))

print(lambd_num)

# even number filter

even_number = list(filter(lambda x: (x % 2 == 0), num))
print(even_number)

# odd number filter

odd_number = list(filter(lambda x: (x % 2 != 0), num))
print(odd_number)
