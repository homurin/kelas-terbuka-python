# alternative way to create a list

# using a range

data_range = range(1, 10, 2)
odd_num = list(data_range)
print('odd num: ', odd_num)

# using for loop, list comprehension

even_num = [i for i in range(0, 10, 2)]
print('even num: ', even_num)

even_num = [i**2 for i in range(0, 10, 2)]
print('even num: ', even_num)

# using if

no_five = [i for i in range(0, 5) if i != 5]
print('remove 5 list: ', no_five)

odd_num = [i for i in range(0, 10) if i % 2 != 0]
print('odd num: ', odd_num)

animal = {'name': ['tiger', 'cats', 'lion', 'eagle', 'lion', 'tiger']}
family = {
    'animal': ['tiger', 'cats', 'lion', 'eagle'],
    'family': ['felix', 'felix', 'felix', 'aves']
}

animal['family'] = [family['family']
                    [family['animal'].index(name)] for name in animal['name']]
print(animal)
