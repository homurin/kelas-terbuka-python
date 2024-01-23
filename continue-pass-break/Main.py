# pass -> will not execute

num = 0

while num < 5:
    num += 1
    if (num == 3):
        pass
    print(num)

# continue

num = 0

while num < 10:
    num += 1
    if (num % 2 != 0):
        continue
        # skip bottom code and repeat loop
    print(f'even num : {num}')

# break

num = 0

while num < 5:
    num += 1
    print(f'current num is {num}')
    if (num == 3):
        print('break the loop')
        break
    print('continue loop')

print('end of program')
