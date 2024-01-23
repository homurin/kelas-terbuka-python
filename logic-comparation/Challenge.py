# Task 1 do
#  - - - - 0 + + + + 5 - - - - - 8 + + + + 11 - - - - -

num = 12

isNotNegative = num >= 0
isLowerThanFour = num <= 5

isGreaterThanSeven = num >= 8
isLowerThanTwelve = num <= 11

print(isNotNegative and isLowerThanFour or isGreaterThanSeven and isLowerThanTwelve)

# Task 2 do
# + + + + 0 - - - - 5 + + + + + 8 - - - -  11 + + + + + +

num = 11

isNegative = num < 0
isGreaterThanFour = num > 4
isLowerThanNine = num < 9
isGreaterThanTen = num > 10

print(isNegative or isGreaterThanFour and isLowerThanNine or isGreaterThanTen)
