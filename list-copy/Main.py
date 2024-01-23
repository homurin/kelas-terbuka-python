# copy a list

olympus_god = ['Posseidon', 'Hades', 'Helios']

# pass by reference

death_god = olympus_god

death_god.remove('Posseidon')

# olympus god got affected

print(f'Olympus god: {olympus_god}')

# the reason, death_god using same address like olympus_god

print(f'olympus_god hex address: {hex(id(olympus_god))}')
print(f'death_god hex address: {hex(id(death_god))}')

# duplicate a list to solve the problem

norse_god = olympus_god.copy()
norse_god = ['magni', 'modi', 'baldur', 'thor', 'odin']

print(f'norse_god hex address: {hex(id(norse_god))}')
print(f'Olympus god: {olympus_god}')
print(f'Norse god: {norse_god}')
