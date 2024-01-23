# string length

full_name = "Mochammad Fajrin"

print(f'{full_name} length: {len(full_name)}')

# check char or string inside string

word = "fajrin"
isExist = word in full_name
print(f'String {word} exists in {full_name} = {isExist} ')

word = "Fajrin"
isExist = word not in full_name
print(f'String {word} exists in {full_name} = {isExist} ')

# repeat string

print("Acumalaka"*7)

# indexing

print(full_name[0])
print(full_name[-1])
print(full_name[0:10])
print(full_name[0:20:2])

# min item
print(f'lower : {min(full_name)}')
# max item
print(f'max : {max(full_name)}')

ascii_code = ord(" ")
print(f'ascii code untuk spasi adalah {ascii_code}')

char = 114
print(f'char untuk ASCII 117 adalah {chr(char)}')

# string method

# count

print(f'total m in {full_name} is {full_name.count("m")}')

# uppercase & lowercase

print(f'{full_name.upper()}')
print(f'{full_name.isupper()}')
print(f'{full_name.lower()}')
print(f'{full_name.islower()}')

# isalpha() => alphabet only

print(full_name.isalpha())

# isalnum() => alphabet and decimal

print(full_name.isalnum())

# isdecimal() => decimal only

print(full_name.isdecimal())

# isspace() => space, tab, newline

print(full_name.isspace())

# istitle() => all word start with uppercase

print(full_name.istitle())

# check component startswith() endswith()

check_start = "Senjougahara Hitagi".startswith("Senjou")

print(f'start {check_start}')

check_end = "Akemi Homura".endswith("Homura")

print(f'end {check_end}')

# join() and split()

my_list = ["Madoka", "Homura", "Sayaka"]
print(" ".join(my_list))

greeting = "Good morning Mr. Griffin"
print(greeting.split())

# character alocation ljust(), center(), rjust()

print(f"'{'Left'.ljust(9)}'")
print(f"'{'Center'.center(40, '*')}'")
print(f"'{'Right'.rjust(9)}'")

center = 'Center'.center(40, '*')
print(center.strip("*"))
