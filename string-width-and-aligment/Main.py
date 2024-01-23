# width and multiline

print('String Data'.center(10, '*'))
data = {
    'name': 'Fajrin',
    'age': 22,
    'height': 176,
}

print(f"""
name   : {data['name']:>6}
age    : {data['age']:>6}
height : {data['height']:>6}
""")
