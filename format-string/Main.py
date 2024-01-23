# thousand ordo

price = 1000000
print(f'milion format: {price:,}')

# decimal number

num = 2001.1112
print(f'decimal: {num:.3f}')
print(f'decimal: {num:.1f}')

# show leading zero

num = 2001.1112
print(f'decimal: {num:9.3f}')
print(f'decimal: {num:09.3f}')
print(f'decimal: {num:010.3f}')

# show + and -

negative_num = -1
positive_num = 1

print(f'Negative : {negative_num}')
print(f'Negative : {negative_num:+d}')
print(f'Positive : {positive_num:+}')

# percentage format

discount = 0.075

print(f'discount : {discount:.1%}')
print(f'discount : {discount:.0%}')

# other num format (binary, octal, hexadecimal)

num = 255

print(f'binary: {bin(num)}')
print(f'octal: {oct(num)}')
print(f'hexadecimal: {hex(num)}')
