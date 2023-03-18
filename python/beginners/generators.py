#!/usr/bin/python3

# yield will work like a return but stop until the next item is asked for
def gen_range(stop, start=1, step=1):
    num = start
    while num <= stop:
        yield num
        num += step

generator = gen_range(10)

x = next(generator)
print(x)
x = next(generator)
print(x)

# these generators can be used inside for loops
for num in gen_range(10, step=2):
    print(num)

# to load a function into the interpretor
# python3.10 -i script_name.py
# custom generators can be turned in to lists
#
generator = gen_range(10)
my_list = list(generator)
print(my_list)

# fibanacci sequence
def gen_fib():
    a, b = 0, 1
    while True:
        a, b = b, a + b
        yield a

fib = gen_fib()
x = next(fib)
print(x)
x = next(fib)
print(x)
x = next(fib)
print(x)
x = next(fib)
print(x)
x = next(fib)
print(x)
x = next(fib)
print(x)
x = next(fib)
print(x)
x = next(fib)
print(x)
x = next(fib)
print(x)
x = next(fib)
print(x)
# now we can calculate the 50th number in the sequence:
print([next(fib) for _ in range(100)][-1])