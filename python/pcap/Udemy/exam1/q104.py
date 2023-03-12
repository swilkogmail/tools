#!/usr/bin/python3
# What is the expected output of the following code?

my_str = "No, I am your father !"
z = my_str.find("a",7,14) # The find() method returns -1 if the value is not found.
print(z)

# The find() method finds the first occurrence of the specified string or character and returns its index.

# The syntax is as follows :

# string.find(value, start, end)  where:

# - value [required] : the string/character to search for

# - start [optional] : the index to start the search (default is 0)

# - end [optional] : the index to end the search (default is the end of the string) - note that this index is excluded from the search.

# In the above question, my_str.find("a",7,14)  will return the index of the first occurrence of the letter "a" in the string  
# my_str, searching between the character at position 7 and the character at position 14 (NOT INCLUDED) (i.e. string 'm your '). 
# Since the letter "a" is not found in the string 'm your ', the return value will be -1.
