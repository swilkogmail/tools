#!/usr/bin/python3
# What is the expected output of the following code, assuming there is no whitespace after the 3rd quote of the first line of code?
my_str = '''
#'''
 
print(len(my_str))

Explanation:
''' allows to delimit a multi-line string.
my_str is a 2-lines string : the first line only includes the special 
character for a new line : \n - it counts as one character. 
The 2nd line only includes the # character (which is not considered as a comment in this case).
So, the total length of the string is : 2.