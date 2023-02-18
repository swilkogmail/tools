#!/usr/bin/python3
# What is the expected output of the following snippet ?
x = 'Yoda 7'
if x.isalpha():
    print(1)
elif x.isdigit():
    print(2)
elif x.isalnum():
    print(3)
else:
    print(4) # Note that a space is neither a digit nor a letter!

# Explanation:
# isalpha() checks if the string contains only alphabetical characters (letters), and returns True or False according to the result.
# isdigit() checks if the string contains only digits, and returns True or False according to the result.
# isalnum() checks if the string contains only digits or alphabetical characters (letters), and returns True or False according to the result.
# Note that a space is neither a digit nor a letter.
# So, the above code returns 4.