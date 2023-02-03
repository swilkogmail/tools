#!/usr/bin/python3
def myfunc(n):
    res = 1
    for i in range(n,n+2,1): # if n = 3 it will loop through twice
        yield res # 1st time return 1, 2nd time return  1(res) x 2
        res*= 2

# it will always return the same as the range function always loops twice n to n+2 (increment by one)
y = [x for x in myfunc(3)]
print(y)            # [1,2]
y = [x for x in myfunc(4)]
print(y)            # [1,2]
y = [x for x in myfunc(5)]
print(y)            # [1,2]
# if we want more in the list we have to increment the '3', i.e. a list of 5 would be n to n+5 (increment by one)
def myfunc(n):
    res = 1
    for i in range(n,n+5,1): # if n = 3 it will loop through twice
        yield res # 1st time return 1, 2nd time return  1(res) x 2
        res*= 2

# it will always return the same as the range function always loops twice n to n+3 (increment by one)
y = [x for x in myfunc(3)]
print(y)            # [1,2]
y = [x for x in myfunc(4)]
print(y)            # [1,2]
y = [x for x in myfunc(5)]
print(y)            # [1,2]

# The yield statement can be used only inside functions. 
# The yield statement suspends the  function execution and 
# causes the function to return the yield's argument as a result. 
# Such a function cannot be invoked in a regular way – 
# its only purpose is to be used as a generator.

# In the above question, when n=3 ,range(n,n+2,1)  
# will generate the following sequence : [3,4] (as always, 
# the end of the range (5)  is excluded from the sequence).

# so for loop for i in range(n,n+2,1):   will go through 2 iterations.

# At the first iteration, res = 1 , so the yield statement generates 1.

# At the 2nd iteration, res= 2*1=2, so the yield statement generates 2.

# Finally, the last statement y = [x for x in myfunc(3)] 
# is a list comprehension which is a way to create a list from an expression.