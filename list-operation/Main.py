data = [1, 2, 3, 4, 5, 1, 4, 1, 3, 4, 5, 5]

# count item

print(f'total item 3 is: {data.count(3)}')
print(f'total item 4 is: {data.count(4)}')

# get item position

angels = ['sachiel', 'shamsiel', 'ramiel', 'gaghiel']
print(f'sachiel adalah angel ke {angels.index("sachiel")}')

# sort item

print(f'before sort: {data}')
data.sort()
print(f'sort data: {data}')

print(f'before sort: {angels}')
angels.sort()
print(f'sort data: {angels}')

# reverse item
data.reverse()
print(f'after reverse : {data}')
data.sort(reverse=True)
print(f'after reverse using sort: {data}')
