#!/usr/bin/python3
# What is the expected behavior of the following snippet?

k = 'Luke'         # line 1
p = 'Leia'         # line 2
def x(k,p='-'):    # line 3
    y = k[0]       # line 4
    return y       # line 5
print(x(k))        # line 6


# Explanation:

# The function x() takes two parameters : k and p ; those parameters have nothing to do 
# with variables k='Luke' and p= 'Leia'. Parameter p is given a default value : '-' ; this means that if 
# the function x() is called without argument p, its default value will be used instead 
# (note that the function x() does not actually use this parameter anyway...).

# So x(k) (where k= 'Luke') is correct and it will return the first letter of the string 'Luke' which is 'L'.