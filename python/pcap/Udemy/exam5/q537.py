#!/usr/bin/python3
# What is the expected output of the following code snippet ?

i=0
while i in range(1,11,2):
    print(i, end='')
else:  # Once the loop has exited, the else: branch gets executed (unless the while loop was terminated with a break statement).
    print('*')

# Explanation:

# With a while loop, the code within the loop will get repeated as long as the condition in the while statement is True.

# Once the loop has exited, the else: branch gets executed (unless the while loop was terminated with a break statement).

# Here variable i gets initialized with a value of 0, and 0 is not in range(1,11,2). So the code within the while branch 
# does not get executed and the code within the else: branch is triggered : * is printed to the monitor.