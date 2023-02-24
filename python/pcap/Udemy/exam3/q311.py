#!/usr/bin/python3
# Consider the code below :

import random
# insert code here
x=[random.randint(1, 10) for i in range(10)]
# : Function randint(1, 10) will produce a random integer which falls in the range [1,10] (with 10 included). 
# So, this code could produce the output shown in the question.
print(x)
x=[random.randrange(1, 10) for i in range(10)]
# : Function randrange(1, 10)  will produce a random integer taken from the range : range(1,10)  - that means 10 is excluded - 
# So, this code cannot produce the output shown in the question (since 10 is one of the number in the expected output)
print(x)
# x=sample([i for i in range(1,11)],10)
# this will produce a list of ten integers taken from the range range(1,11) - 
# but each integer is only selected once (that's what the function sample() does).  
# So, this code cannot produce the output shown in the question since 3 is repeated twice in the expected output.
print(x)
x=[int(random.random()*10) for i in range(10)]
# int(random.random()*10)  will return an integer (thanks to the int() function) 
# between 0 and 10 (excluded) - So, this code cannot produce the output shown in the question (since 10 is one of the number in the expected output).
print(x)

for i in range(10): # loop through from 0,9
    print(i)
for i in range(1,10): # loop through from 1,9
    print(i)