#!/usr/bin/python3
# Consider the code below :

from random import random
# The random() function (from the random module) returns a random floating point number in the range [0.0, 1.0) (in other words: (0.0 <= x < 1.0)
from math import floor
# The floor() method (from the math module) returns the largest integer not greater than x.
# For example :
# floor(3.4) returns 3
# floor(-3.6) returns -4

# So, floor(random()*10)  would returns an integer between 0 and 9 (10 is not included since 1.0 is not included in the range of the random() function).

for i in range(5): # return 0,1,2,3,4
    print(floor(random()*10),end=',')

#it picks five numbers 0.0 - 0.9 at ramdom and muiplies them by 10, i.e. 4 numbers between 1 and 9

# What would be a possible result from the above code ? (Pick 2)

print("Just random:")
for i in range(5): # return 0,1,2,3,4
    print(random())

print("Random x 10")
for i in range(5): # return 0,1,2,3,4
    print(random()*10)

print("Random + foor")
for i in range(5): # return 0,1,2,3,4
    print(floor(random()*10))

print("Random + foor in a list")
for i in range(5): # return 0,1,2,3,4
    print(floor(random()*10),end=',')
