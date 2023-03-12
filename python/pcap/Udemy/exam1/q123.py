#!/usr/bin/python3
Question 19: Incorrect
# What is the expected output of the following code snippet ?

def sum_list(args, fun): # The function sum_list() takes two parameters: an iterable (ex : a list) and a function.
    z = 0
    for x in args:
        z = z + fun(x)
    return z
 
print(sum_list([ex//2 for ex in range(5)], lambda x: 1 if x>1 else 0))

# ex//2 for ex in range(5) returns a list of 0,0,1,1,2 (the floor of 0/2,1/2,2/2,3/2,4/2)
# this list is fed into sum_list
# the function lambda x: 1 if x>1 else 0 is called with each of the lists items
# and return 1 if x> 1 and 0 if not

for ex in range(5)
    print(ex)

# sum_list([ex//2 for ex in range(5)], lambda x: 1 if x>1 else 0) is an invocation of the function sum_list()  with :

# - the iterable parameter as : [ex//2 for ex in range(5)] -> this is a list comprehension which returns : 
# [0, 0, 1, 1, 2] (// is the floor division which is an operation that divides two numbers and rounds the result down to the nearest integer).

# - the function parameter as: a lambda function : this function simply returns 1 if its 
# argument is greater than 1, else it returns 0.

# So sum_list() will apply the lambda function to all elements of [0, 0, 1, 1, 2] and returns the overall sum.

# Lambda function applied to the first element of [0, 0, 1, 1, 2] will return 0.

# Lambda function applied to the second element of [0, 0, 1, 1, 2] will return 0.

# Lambda function applied to the 3rd element of [0, 0, 1, 1, 2] will return 0.

# Lambda function applied to the 4th element of [0, 0, 1, 1, 2] will return 0.

# Lambda function applied to the 5th element of [0, 0, 1, 1, 2] will return 1.

# And overall sum of those results will be 1.

# So final answer is :

# 1