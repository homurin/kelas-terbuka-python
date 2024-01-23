# triangle looping

# for loop

print('for loop')

for i in range(6):
    print('*'*i)

# while

print('while loop')

count = 1

while count <= 5:
    print('*'*count)
    count += 1

# only odd num

print('only odd num')

num = 0

while num < 5:
    num += 1
    if (num % 2 == 0):
        continue
    print('*'*num)

# equilateral triangle


print('equilateral triangle')

width = 10
count = 1
blank_space = width

while True:
    if (count % 2 != 0):
        print(" "*blank_space, "*"*count)
        count += 1
        blank_space -= 1
        continue
    count += 1
    if (count >= width):
        break

print('rhombus shape')

width = 10
count = 1
blank_space = width

while True:
    if (count % 2 != 0):
        print(" "*blank_space, "*"*count)
        count += 1
        blank_space -= 1
        continue
    count += 1
    if (count >= width):
        break
while True:
    if (count % 2 != 0):
        print(" "*blank_space, "*"*count)
        count -= 1
        blank_space += 1
        continue
    count -= 1
    if (blank_space > width):
        break
