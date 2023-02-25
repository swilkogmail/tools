#!/usr/bin/python3
# What is the expected output of the following code?

x = '\t\\'*2 + '\t'
print(len(x.split('t')))


# Explanation
# Knowledge Area : Strings
# Topic : escape character (\), len(), split()
# Explanation:
# In a string, the \ character (called "escape character") is used to insert characters 
# that are illegal in a string or to insert other special characters (like a new line).
# For example '\\' will insert one backslash (\).
# '\t' will insert a tab.
# string * int will repeat that string int times.
# string + string will concatenate the 2 strings.
# so, x returns a string with 5 tabs and 2 backslashes.
# The split() method is a string method and will return a list where the elements of the list 
# are the result of splitting the string with a specified character separator. By default the character separator is any space.
# So : x.split('t') will return a list with only element since there is no character 't' in x ('\t'  is a tab).
# Finally, len(x.split('t')) returns 1.
# Try it yourself:
# x = '\t\\'*2 + '\t'
 
print(x)               # 	\	\	
print(x.split('t'))    # ['\t\\\t\\\t']
print(len(x.split('t'))) # 1