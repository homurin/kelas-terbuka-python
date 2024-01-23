# bitwise, biner, binary

a = 9
b = 5

# bitwise OR (|)

c = a | b
print("\n=====OR=====")
print(f'value : {a}, binary:\t{format(a, "08b")}')
print(f'value : {b}, binary:\t{format(b, "08b")}')
print("========================== (|)")
print(f'value : {c}, binary:\t{format(c, "08b")}')

# bitwise AND (&)

c = a & b

print("\n=====AND=====")
print(f'value : {a}, binary:\t{format(a, "08b")}')
print(f'value : {b}, binary:\t{format(b, "08b")}')
print("========================== (&)")
print(f'value : {c}, binary:\t{format(c, "08b")}')

# bitwise XOR (^)

c = a ^ b
print("\n=====XOR=====")
print(f'value : {a}, binary:\t{format(a, "08b")}')
print(f'value : {b}, binary:\t{format(b, "08b")}')
print("========================== (^)")
print(f'value : {c}, binary: {format(c, "08b")}')

#  bitwise NOT (~)

c = ~a
print("\n=====NOT=====")
print(f'value : {a}, binary:\t{format(a, "08b")}')
print("========================== (~)")
print(f'value : {c}, binary:\t{format(c, "08b")}')

# use these tricks for flip

d = 0b00001001
e = 0b11111111
print("========================== (^)")
print(f'value : {d}, binary:\t{format(d, "08b")}')
print(f'value : {e^d}, binary:\t{format(e^d, "08b")}')

#  shifting

# shift right (>>)

c = a >> 2
print("\n=====Shift Right=====")
print("========================== (>>)")
print(f'value : {a}, binary:\t{format(a, "08b")}')
print(f'value : {c}, binary:\t{format(c, "08b")}')

# shift left (<<)

c = a << 2
print("\n=====Shift Right=====")
print("========================== (<<)")
print(f'value : {a}, binary:\t{format(a, "08b")}')
print(f'value : {c}, binary:\t{format(c, "08b")}')
