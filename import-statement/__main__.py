# import all
from science.math import divide as div
from science.math import substract
import time as tm
import science
from science import *

# import some function or variable

start_time = tm.time()


# using alias


print(science.math.add(1, 2, 3, 4, 5))
print(substract(10, 5))
print(div(10, 5))

finish_time = tm.time()

exec_time = finish_time - start_time

print(f'execution time: {exec_time}')
