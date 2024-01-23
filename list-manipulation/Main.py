# add an item to the list according to position

angels = ['sachiel', 'shamsiel', 'ramiel', 'israfel']

# before

print(angels)

angels.insert(3, 'gaghiel')

# after

print(angels)

# add an item to latest list index

angels.append('sandhalphone')
print(angels)

# merge two list into one

seeds = ['adam', 'lilith']
angels.extend(seeds)

print(angels)

# change item

angels[4] = 'isrofel'
print(angels)

# remove item

angels.remove('adam')
print(angels)

# remove latest item

last_item = angels.pop()
print(angels)
print(f'removed item is {last_item}')
