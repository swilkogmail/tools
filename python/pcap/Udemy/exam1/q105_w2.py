#!/usr/bin/python3
# What is the expected output of the following snippet?

my_str = 'Luke !!\n'
z = my_str.index('n')
print(z)

# Explanation:

# The index() method finds the first occurrence of the specified string or character and returns its index.

# The index() method raises an exception if the value is not found.

# The syntax is as follows :

# string.index(value, start, end)  where:

# - value [required] : the string/character to search for

# - start [optional] : the index to start the search (default is 0)

# - end [optional] : the index to end the search (default is the end of the string) - note that this index is excluded from the search.

# In the above question, my_str.index('n')  will return the index of the first 
# occurrence of the letter "n" in the string  my_str, searching between the character at 
# position 0 and the last character of the string (i.e. the whole string). 
# In the string 'Luke !!\n' , '\n' is actually the code for a new line (note that escape character '\'); 
# this is not representing the character 'n'. So character 'n' is NOT in the string 'Luke !!\n' and my_str.index('n')  will raise an exception.



# Note : other escape codes to know:

# \'  : single quote (')
# \\ : backslash (\)
# \n : new line
# \r : carriage return
# \t : tab
# \b : backspace