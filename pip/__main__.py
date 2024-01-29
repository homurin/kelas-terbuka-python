import numpy as np

# list vs np.array()

print(f"{'='*50:<50}")
my_list = [1, 2, 3, 4, 5]
print(f'this is list: {my_list}')
print(my_list)
print(my_list[0])

# print(my_list**2) <- this will return error
print('error :(')
print(f"{'='*50:<50}")

# vector

my_vector = np.array([1, 2, 3, 4, 5])
print(f'this is np.array(): {my_vector}')
print(my_vector)
print(my_vector[0])
print(my_vector**2)

# matrix

my_matrix = np.array([(1, 2), (3, 4)])
print(f'matrix: \n{my_matrix}')
print(f'matrix: \n{my_matrix**2}')

# zeros

my_zeros = np.zeros((2, 2))
print(f'my zeros: \n{my_zeros}')

# ones
my_ones = np.ones((2, 2))
print(f'my ones: \n{my_ones}')

total = my_matrix + my_matrix**2 + my_ones
print(f'total: \n{total}')
