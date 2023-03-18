#!/usr/bin/python3
# You want to iterate through all characters of a string (variable named my_string) and print only the 
# characters that are numbers (0..9) on one single line.

# Which code snippet below will achieve this requirement ?

# Explanation:

# for x in seq: allows to loop through each elements of a sequence seq. This sequence can be a list, a string, a range, etc...

# To loop through each character of string my_string, the code statement should be : for x in my_string:

# while x in my_string: --> will raise an exception

# for each x in my_string: --> will raise an exception (there is no for each loop in Python)

# Finally, to ensure the characters are printed on one single line, you need to use the end keyword argument of the print() function (by default, end = '\n' ( new line))