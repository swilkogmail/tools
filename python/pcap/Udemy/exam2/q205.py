#!/usr/bin/python3
# What is the expected output of the following code snippet ?

x = "Leo and Chloe love apple pie"
y = x.split() # The split() method splits a string into a list.
z = sorted(y) # sorted()  is a function that will return a new sorted list (ascending order by default).  When sorting strings, 
              # keep in mind that the sorting is done using the 
              # Unicode point of the first letter in each strings and that uppercase letters have a lower Unicode point than lowercase letters.
print(z[1])   # Based on this, the answer is : Leo




# The syntax is as follows: string.split(separator, max)  where :

# string : the string to split

# separator: optional separator to use when splitting the string. Default separator is a whitespace.

# max : optional maximum number of splits to generate. Default value is -1 which is "no limit".

# Refer to the section below to see the intermediate output of each line of code and see how split() and sorted() work on the given string.

