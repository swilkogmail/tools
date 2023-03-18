#!/usr/bin/python3

# Which statement about Python classes is correct  ?

# A class must have a constructor.
# (Incorrect)

# A class has a method named __module__() which returns the name of the module in which the class has been declared.

# A class contains a property named __name__ which stores the name of the class.
# (Correct)

# A class contains a property named __bases__ which is a tuple containing the name of the class's superclasses.


# Explanation:
# Let 's review each suggested answers:
# --> A class must have a constructor.
# This is incorrect : a class can be defined without a constructor.
# --> A class contains a property named __name__ which stores the name of the class.
# This is correct
# --> A class contains a property named __bases__ which is a tuple 
# containing the name of the class's superclasses.
# That is incorrect : this tuple contains the actual class's superclasses, not their names.
# --> A class has a method named __module__() which returns the name of the 
# module in which the class has been declared.
# That is incorrect : a class has a property named __module__ (not a method) which 
# returns the name of the module in which the class has been declared.

class A:
    # class does not have any constructor
    pass
 
class B(A):
    # class does not have any constructor
    pass
 
print(B.__name__)    # B
print(B.__bases__)   # (<class '__main__.A'>,)
print(B.__module__)  # __main__