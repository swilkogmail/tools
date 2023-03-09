#!/usr/bin/python3
# What is the expected output of the following code if :

# (1) the user enters 10/2 when prompted ?

# (2) the user enters 3.1 when prompted ?

x = input("Enter number : ")
print(int(x))

# Explanation:

# The input() function returns a string.

# The  int() function returns an integer object from any number or string - if the function 
# cannot convert the object to an integer, an exception is raised.

# Here in the above question, when the user enters 10/2, this will 
# be treated as a string and the int() function will not be able to convert this string into an integer --> an exception will be raised.

# When the user enters 3.1 , this is also a string : the int() function 
# will not be able to convert this string into an integer --> an exception 
# will be raised. If this had been a float, then int(3.1) would have returned 3.