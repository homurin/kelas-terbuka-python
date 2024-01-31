from os import path
# read external file

file_path = path.abspath(__file__)
dir_path = path.dirname(file_path)

buffer = open(f'{dir_path}/data.txt', mode='r')
print(f'is file readable: {buffer.readable()}')
print(f'is file writable: {buffer.writable()}')

# read all line

# print(buffer.read())

# read each line

# print(buffer.readline(), end="")
# print(buffer.readline(), end="")

# read all line as list

print(buffer.readlines())

print(f'is file closed: {buffer.closed}')

buffer.close()

print(f'is file closed: {buffer.closed}')

# automatic close

with open(f'{dir_path}/data.txt', mode='r') as file_buffer:
    content = file_buffer.readline()
    print(content, end="")
    print(f"is file closed: {file_buffer.closed}")

# automatic closed outside with block

print(f"is file closed: {file_buffer.closed}")
