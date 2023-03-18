#!/usr/bin/python3
# What is the expected output of the following snippet ?

x='luke'
y='Luke'
 
if x > y: # l > l true
    print('Han')
elif x < y: # l < L false
    print('Leia')
elif x==y: # l = L false
    print('Ben')
else:
    print('Chewie')

# upper case is less that lower case

# Explanation:
# Comparing strings is determined by comparing the first different character in both strings (using ASCII/UNICODE code).
# String comparison is always case-sensitive (upper-case letters are taken as lesser than lower-case).
# So 'luke' > 'Luke' is True.
# 'luke' < 'Luke' is False.
# 'luke' == 'Luke' is False.