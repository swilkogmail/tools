#!/usr/bin/python3
# What is the output of the following snippet ?

def myfunc(n):
    res = ord('A')
    for i in range(0,n,2):
        yield chr(res)
        res+=2
 
y = [x for x in myfunc(10)]
 
print(y)


# Explanation:

# The yield statement can be used only inside functions. The yield statement suspends the  
# function execution and causes the function to return the yield's argument as a 
# result. Such a function cannot be invoked in a regular way – its only purpose is to be used as a generator.

# A generator can be used to produce a list within a list comprehension.

# In the above question, when n=10 ,range(0,n,2)  will generate the following sequence : [0,2,4,6,8] 
# (as always, the end of the range (10)  is excluded from the sequence).

# so for loop for i in range(0,n,2):   will go through 5 iterations.

# Function ord('char') will return the Unicode code of character char.

# The function chr(i) will do the opposite : it will return the character with the Unicode code i.

# So, at the first iteration, res  has the value of ord('A')  (there is no need to know the actual 
# Unicode code of A to answer this question correctly) , so the yield statement generates chr(ord('A')) which is letter A.

# At the 2nd iteration, res is incremented by 2 , so the yield statement generates chr(ord('A') + 2)  
# which is letter C . And so on, until the last iteration which generates letter I.

# Finally, the last statement y = [x for x in myfunc(10)]   is a list comprehension which is a
#  way to create a list from an expression.

# Using the myfunc(10) as the generator, [x for x in myfunc(10)]  will return each yield's 
# argument from myfunc(10) as a list element . The resulting list is : ['A', 'C', 'E', 'G', 'I'] .