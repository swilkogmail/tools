#!/usr/bin/python3
# How many stars will the following snippet print to the monitor?

x = 8
while x > 0:
    print('*')
    x //= 2  # The // operator is also called floor division : 8//2 =4 , 4//2=2, 2//2=1 and 1//2=0.
else:
    print('*')  # At that point the code under the else: clause will execute : that's a 5th (and last) star.

# Explanation:

# In a while-else loop, the code under the else: clause will execute once the condition of the while statement becomes False.

# The // operator is also called floor division : 8//2 =4 , 4//2=2, 2//2=1 and 1//2=0.

# The while loop will go through 4 iterations until condition x > 0 becomes False. That will produce 4 stars.

# At that point the code under the else: clause will execute : that's a 5th (and last) star.