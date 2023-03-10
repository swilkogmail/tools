#!/usr/bin/python3
# How many stars will the following code print to the monitor?

x = 1
while x < 5:
    print('*')
    x = x << 1  # << is a bitwise operator :  x = x << 1  will double the value of x
else:
    print(2*'*')
finally:
    print(3*'*')


# Explanation:

# The above code has a syntax error since finally: works with a try: block, not with a while-else loop.

# If the 2 last lines of code were removed, then the result would have been five stars printed out 
# on the screen : three stars from within the while loop and two from within the else: clause.

# << is a bitwise operator :  x = x << 1  will double the value of x