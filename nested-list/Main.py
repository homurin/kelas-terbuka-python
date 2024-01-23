from copy import deepcopy

# nested deep copy list

data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# shallow copy

data_copy = data.copy()

# list iw duplicated

print(f'data list address: {hex(id(data))}')
print(f'data list copy address: {hex(id(data_copy))}')


# each item inside list not duplicated
# each item address remain same

print(f'data[0][1] address: {hex(id(data[0][1]))}')
print(f'data_copy[0][1] address: {hex(id(data_copy[0][1]))}')

# solution is using deepcopy
# now each list has different address

data_deepcopy = deepcopy(data)

print(f'data[0][1] address: {hex(id(data[0]))}')
print(f'data_copy[0][1] address: {hex(id(data_deepcopy[0]))}')
