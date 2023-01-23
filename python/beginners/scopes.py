#!/usr/bin/python3
# conditionals and loops do not define their own scope
# functions define their own scope
# the global key word can be used
# although if there is a parameter set (called by a function) this will always win

y = 5

def set_x(y):
    print("Inner y: ", y)
    x = y
    # global y
    y = x

set_x(10)

print("Outer y: ", y)