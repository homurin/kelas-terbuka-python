from os import path

file_path = path.abspath(__file__)
dir_path = path.dirname(file_path)

# write mode

with open(f"{dir_path}/writed_file.txt", mode="w", encoding='UTF-8') as buffer:
    buffer.write('DEBIAN')

# overwrite writed file

with open(f"{dir_path}/writed_file.txt", mode="w", encoding='UTF-8') as buffer:
    buffer.write('ARCH')

# append mode

with open(f"{dir_path}/writed_file.txt", mode="w", encoding='UTF-8') as buffer:
    buffer.write('ARCH\n')
with open(f"{dir_path}/writed_file.txt", mode="a", encoding='UTF-8') as buffer:
    buffer.write('DEBIAN\n')
with open(f"{dir_path}/writed_file.txt", mode="a", encoding='UTF-8') as buffer:
    buffer.write('FEDORA')

# r+ (override)

with open(f'{dir_path}/write-with-r+.txt', mode='w', encoding='UTF-8') as buffer:
    buffer.write('UBUNTU\n')
    buffer.write('UBUNTU\n')
    buffer.write('UBUNTU\n')

with open(f'{dir_path}/write-with-r+.txt', mode='r+', encoding='UTF-8') as buffer:
    buffer.write('UBUNTU\n')
    buffer.write('DEBIAN\n')

with open(f'{dir_path}/write-with-r+.txt', mode='r+', encoding='UTF-8') as buffer:
    buffer.write('UBUNTU\n')
    buffer.write('DEBIAN\n')
    buffer.write('ARCH LINUX\n')

with open(f'{dir_path}/write-with-r+.txt', mode='r+', encoding='UTF-8') as buffer:
    buffer.write('FEDORA\n')


# readfile

with open(f'{dir_path}/writed_file.txt', mode='r') as buffer:
    print(buffer.read())
