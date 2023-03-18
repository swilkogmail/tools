#!/usr/bin/python3
# Which statement(s) below will return True ?

# Explanation:

# The bool() function converts a value to Boolean (True or False).

# The following values are considered false in Python:

# - None

# - False

# - Zero (any numeric type)

# - Empty sequence (list, tuple, empty string, etc...). For example, (), [], ''.

# - Empty mapping. For example, {}



# In the above question :

# - 'False' is a non-empty string, so bool('False')  returns True

# - 4**0 returns 1 - so bool(4**0) returns True

# Try it yourself:

print(bool([]))        # False
print(bool('False'))   # True
print(bool(4**0))      # True
print(bool(None))      # False