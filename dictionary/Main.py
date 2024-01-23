# dict -> associative array
# identifier -> key

cat = {
    'name': 'sumbul',
    'age': 8,
    'race': 'aves',
    'friends': ['ahmad', 'hamzah']
}

print(cat['name'])
print(cat['age'])
print(cat['race'])
print(cat['friends'])

# dictionary operator

person = {
    'username': 'Ahmad Kasim',
    'age': 25,
    'planet': 'atatatiga',
    'minions': ['probe', 'computer']
}

# length dict

PERSONLEN = len(person)

print('person length is: ', PERSONLEN)

# check is key exist

KEY = 'username'
is_key_exist = KEY in person
print(f'is {KEY} exist in person dictionary: {is_key_exist}')

KEY = 'buwung'
is_key_exist = KEY in person
print(f'is {KEY} exist in person dictionary: {is_key_exist}')

# access dict value using get

print(person.get('username'))
print(person.get('age'))
print(person.get('minion', False))

# update dict data

person['username'] = 'AHMAD'
print(person.get('username'))

# elegant way

person.update({'username': 'Adudu'})
print(person.get('username'))

# delete a key

del person['minions']
print(person)
