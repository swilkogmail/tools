#!/usr/bin/python3
# Consider the code below :

def my_func(n):
    pwr = 1
    for i in range(n):
        print(f"{pwr} x {2}")
        yield pwr
        # next line is out od scope of the yield, only pwr is returned
        pwr *= 2
 
t = [x for x in my_func(5)]
print(t)

# pwr is returned each time before the pwr is factored in