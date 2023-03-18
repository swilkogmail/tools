#!/usr/bin/python3
# What is the expected output of the following code ?
mystring='Skywalker'
n=0
while n<=len(mystring):
    print(mystring[n],end='')
    if mystring[n]=='y':
        break
    else:  
        continue # continue  will stop the current iteration and continue with the next 
                 # iteration. So the n+=1 statement does not get executed and n remains with a value of 0.
    n+=1
else:
    print(mystring[0])

# Explanation:

# The while loop will repeatedly execute the code in its block until the condition n<=len(mystring) is False.

# The len() function applied to a string will return the number of characters in a string.

# In this case, len(mystring) is  9.

# Initially n is set to 0. So, at the first pass the condition n<=len(mystring) is True and the code block underneath while gets executed:

# The very first statement in this code block is print(mystring[n],end='')  which will print the first letter of Skywalker which is S .

# The if..else conditional statement compares the value of  mystring[n] 
# (which is S at the very first pass since n=0 and slicing a string at position 0 
# returns the first character of the string) with character y. Since mystring[n]=='y' is False 
# the code block underneath the else statement gets executed.

# continue  will stop the current iteration and continue with the next iteration. So the n+=1 statement does not get executed and n remains with a value of 0. 
# The code block underneath while gets executed a second time and since n has still 
# a value of 0 the letter S is printed again and so on...in an infinite loop.

# To avoid this infinite loop, the n+=1 statement would need to be moved to a section of the code that is reacheable.