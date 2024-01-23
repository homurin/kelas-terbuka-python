print("object identity (is)")

x = 5
y = 5

# if object has same value, python will save it at same memory
# for better memory management

print(f'x value = {x}, id = {hex(id(x))}')
print(f'y value = {y}, id = {hex(id(y))}')

result = x is y
print(f"x is y = {result}")
