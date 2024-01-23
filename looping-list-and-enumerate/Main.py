# list comprehension

god_of_war = ['Ares', 'Tyr', 'Indra', 'Horus']

print('God of War')
[print(name) for name in god_of_war]
gods = [name for name in god_of_war]

print(gods)

# enumerate

print('God of War')
for index, name in enumerate(god_of_war):
    print(f'{index}. {name}')
