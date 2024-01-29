import datetime as dt
import time
import io
import os

curr_mills = time.time()
curr_time = dt.datetime.fromtimestamp(curr_mills)
print(f'current milisecond: {curr_mills}')
print(f'year: {curr_time.year}')
print(f'month: {curr_time.month}')
print(f'day: {curr_time.day}')
print(f'fulldate: {curr_time.date()}')

curr_file = os.path.abspath(__file__)
curr_path = os.path.dirname(curr_file)

print(f'current file path: {curr_file}')
print(f'current dir path: {curr_path}')

buffer = io.open(f'{curr_path}/README.md', 'r')
print(buffer.read())
