#!/usr/bin/python3
# What is the expected output of the following code ?

for i in range(1,20):
    if i%7 == 0: # loop until we hit 7 and then exit so 1,3,5 (7 not included)
        break
    elif i%2 == 0: # even numbers
        continue # are ignored
    else:
        print(i, end='')
else:
    print(8) # - at i=7, the break statement stops the loop and the code within the else statement does not get executed.

# Explanation:

# The for-else loop executes a set of statements for a number of times - the block of code within the 
# else statement is executed if it has not been terminated by break.

# The break statement stops the loop - and the block of code within the else statement does not get executed.

# The continue statement stops the current iteration, and continue with the next.

# So, in the code snippet above :

# - all odd numbers get printed (1,3,5)

# - all even numbers get skipped (continue statement)

# - at i=7, the break statement stops the loop and the code within the else statement does not get executed.

# The end result is 135 printed to the monitor.