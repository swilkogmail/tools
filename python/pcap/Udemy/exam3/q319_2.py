#!/usr/bin/python3
# What is the expected output of the following code snippet ?
dict = {1 : 'France' , 2: 'USA', 3: 'Japan', 4 : 'Canada' }
 
try:
    for i in range(5):
        if not(dict[i+1].isalpha()):
            raise ValueError
    print("Done")
except ValueError:
    print("ValueError")
except IndexError:
    print("IndexError")
except KeyError:  # KeyError exception will be raised, and KeyError will be printed.
    print("KeyError")

# Explanation
# Knowledge Area : Exceptions
# Topic : KeyError , IndexError
# Explanation:
# KeyError is a concrete exception raised when there is an attempt to access a collection's 
# non-existent element (for example : a dictionary's element). KeyError is a subclass of LookupError.
# In the above code, in the for loop, when i=4, dict[5] does not exist (5 is not an existing key in this dictionary)  - so the
# KeyError exception will be raised, and KeyError will be printed.
# Note that  IndexError is another subclass of LookupError but it is raised when there 
# is an attempt to access a non-existent sequence's element (for example a list's element).
# Try it yourself:
dict = {1 : 'France' , 2: 'USA', 3: 'Japan', 4 : 'Canada' }
 
try:
    for i in range(5):
        if not(dict[i+1].isalpha()):
            raise ValueError
    print("Done")
except ValueError:
    print("ValueError")
except IndexError:
    print("IndexError")
except KeyError:
    print("KeyError")        # KeyError