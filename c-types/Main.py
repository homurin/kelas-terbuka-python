from ctypes import c_double as double, c_char as char

data_double = double(10)
data_char = char(11)

print(f"typeof {data_double} is { type(data_double) }")
print(f"typeof {data_char} is { type(data_char) }")
