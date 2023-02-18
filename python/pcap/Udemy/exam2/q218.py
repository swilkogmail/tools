#!/usr/bin/python3
# What is the expected output of the following snippet ?

x='luke'
y='Luke'
 
if x > y:
    print('Han')
elif x < y:
    print('Leia')
elif x==y:
    print('Ben')
else:
    print('Chewie')

# Explanation:
# Comparing strings is determined by comparing the first different character in both strings (using ASCII/UNICODE code).
# String comparison is always case-sensitive (upper-case letters are taken as lesser than lower-case).
# So 'luke' > 'Luke' is True.
# 'luke' < 'Luke' is False.
# 'luke' == 'Luke' is False.