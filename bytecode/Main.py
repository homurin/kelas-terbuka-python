import time

# run python3 -m py_compile interpreter.py for compiling pyton script to bytecode
# the script above will generate __pycache__ folder

start_time = time.time()

print("hello world")
for i in range(0, 100000):
    print("compiling...")

print(f'execution time is {time.time() - start_time} seconds')
