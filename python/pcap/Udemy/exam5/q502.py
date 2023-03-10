#!/usr/bin/python3
# How many stars will the following snippet print to the monitor?

i = 6
while i > 0:
    i -= 2 # 1. i = 4, 2 i = 2
    print('*') # * **
    if i == 2:
        break  # when i = two then it beaks and doesn't return the else
    else:
        continue
    print('*')
else:
    print('*')