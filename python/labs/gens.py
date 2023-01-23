#!/usr/bin/python3
def char_range(start, stop, step=1):
    start_code = ord(start)
    stop_code = ord(stop)
    for value in range(start_code, stop_code + 1, step):
        yield chr(value)

generator = char_range('a','e')

x = next(generator)
print(x)
x = next(generator)
print(x)
x = next(generator)
print(x)
x = next(generator)
print(x)
x = next(generator)
print(x)


# backwards iteration
def char_range(start, stop, step=1):
    start_code = ord(start)
    stop_code = ord(stop)

    if start_code > stop_code:
        step *= -1 # miltiply by -1 as this will assign it a neg step code

    for value in range(start_code, stop_code -1, step):
        yield chr(value)

generator = char_range('e','a')

x = next(generator)
print(x)
x = next(generator)
print(x)
x = next(generator)
print(x)
x = next(generator)
print(x)
x = next(generator)
print(x)