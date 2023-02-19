#!/usr/bin/python3
Consider the code below:

x = 'Cheabacca'
# Insert line of code here.

# Which snippet would you insert in order for the program to output the following result:
# Chewbacca

# Explanation:
# The swap() method is made up and does not exist as a built-in string method.
# The find() method does exist but it looks for a substring and returns the 
# index of first occurrence of this substring. So, this would not produce 
# the expected output (plus x.find('a','w',4) is not the correct syntax anyway).
# So that leaves the replace() method.
# The  replace() method returns a copy of the original string in which all 
# occurrences of the first argument have been replaced by the second argument. 
# An optional third argument (a number) is used to limit the number of replacements.
# That's exactly what is needed here : we need to replace character 'a' with 
# 'w' and we need to only do it once - which translates to:
# x.replace('a','w',1)