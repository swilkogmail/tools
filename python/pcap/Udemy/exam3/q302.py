#!/usr/bin/python3
# Which statement is true about the two objects below ? (Pick two)
str1='Hello'
str2='Hello'

# Explanation:
# A string is immutable and if you create two strings with the same value they will point to the same object.
# id() function returns the identity of the object. This is an integer that is unique for the 
# given object and remains constant during its lifetime.
# Since str1 and str2 point to the same object, their identity is the same.
# so id(str1) == id(str2) is True
# Obviously  id(str1) != id(str2)   is False
# str1[::1] is a slicing operation on the string str1  It returns all characters from the first 
# index of the string to the last index, with a step of 1 character - in other words, the whole 
# string which is Hello. And so str1[::1] == str2 is True.
# Finally, the is and is not operators check whether both operands refer to the same object or not.
# As explained above, str1 and str2 do refer to the same object, so str1 is str2  is True and  str1 is not str2 is False.

Try it yourself:
str1='Hello'
str2='Hello'
 
print(id(str1))                # 140473762198000
print(id(str2))                # 140473762198000
print(id(str1) == id(str2))    # True
print(id(str1) != id(str2))    # False
print(str1[::1])               # Hello
print(str1[::1] == str2)       # True
print(str1 is str2)            # True
print(str1 is not str2)        # False