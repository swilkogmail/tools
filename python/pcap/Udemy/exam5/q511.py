#!/usr/bin/python3
# What is the output of the following snippet?

def myfun(n):
    if n%2 == 0:
        return 0
    else:
        return 1 + myfun(n+1)
 
 
print(myfun(5))

# Explanation:

# The above function uses recursion, which means the function calls itself.

# To get the output of the function you simply have to go through each call of the function until a result is returned.

# In the case of the above question, you start with n=5:

# Since 5 is an odd number (5%2 returns 1), statement return 1 + myfun(n+1)  gets executed.

# To get the output of myfun(n+1), you need to go through the function logic again with n=6.

# Since 6 is an even number (6%2 returns 0), statement return 0)  gets executed.

# So, now we can calculate the output of return 1 + myfun(n+1)  when n was 5 : that's 1 + 0 , i.e. 1.

# So, print(myfun(5)) will simply print 1 .