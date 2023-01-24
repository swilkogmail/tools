#!/usr/bin/python3
# conditionals and loops do not define their own scope
# functions define their own scope
# the global key word can be used
# although if there is a parameter set (called by a function) this will always win

y = 5

def set_x(y):
    print("Inner y: ", y)
    x = y
    # global y can't be accessed as we have a parameter with the same name
    # parameters always win
    y = x

set_x(10)

print("Outer y: ", y)

def set_z(z):
    x = z
    global y
    global a # this is the more useful case as this is now accessible outside the function
    y = x
    a = 7

print("y before set_z: ", y)
set_z(10)
print("y after set_z: ", y)

print("a after set_z: ", a)