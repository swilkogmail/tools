#!/usr/bin/env python3
x = True
y = False
z = False

if not x or y:
    # not True or False
    # False or False
    # False
    print(1)
elif not x or not y and z:
    # not True or not False and False
    # False or (True and False)
    # False or (False)
    # False
    print(2)
elif not x or y or not y and x:
    # not True or False or not False and True
    # False or False or True and True
    # False or False or (True and True)
    # False or False or True
    # True
    print(3)
else:
    print(4)