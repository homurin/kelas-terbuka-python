# + + + 3 - - - - - 10 + + +

input_user = 11

isLowerThanTwo = input_user < 3
isGreaterThanNine = input_user > 9

isCorrect = isLowerThanTwo or isGreaterThanNine
print(f'input user is {isCorrect}')

# - - - 3 + + + + 10 - - - -

input_user = 11

isGreaterThanTwo = input_user > 2
isLowerThanEleven = input_user < 11

isCorrect = isGreaterThanTwo and isLowerThanEleven
print(f'input user is {isCorrect}')
