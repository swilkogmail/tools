#!/usr/bin/python3
# What is the expected output of the following code ?

my_text = "Osaka is a city in Japan"
print(my_text.rfind('a', 3, -3))


# Explanation:

# The rfind() method returns the highest index of the substring (if found). If not found, it returns -1.

# The syntax of rfind() is:

# str.rfind(sub, start, end ) where:

# - sub :  It's the substring to be searched in the str string.

# - start and end (optional) - substring is searched within str[start:end]

# In the above question, character a, is searched in string my_text  starting at index 3 and up to 
# index -3 (not included). The highest index of character a  within that substring is returned, which is index 20.

# Try it yourself:

# my_text = "Osaka is a city in Japan"
# print(my_text.rfind('a', 3, -3)) # 20
# Question ID: Q415