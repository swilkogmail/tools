#!/usr/bin/python3
# What is the expected output of the following code?
class Jedi:
    def __init__(self, name):
        self.name = name
    # def __str__(self):  # To get a result different from the default string above, the __str__() method would need to be defined in the Jedi class.
    #     return self.name
    def Print(self):
        return self.name
 
 
Luke = Jedi('Luke')
print(Luke)
print(Luke.name)

# Explanation:

# The __str()__ method is not defined for object Luke of class Jedi.

# So invocating the print() function on object Luke will invoke the default __str()__ method 
# which returns the following string :

# <__main__.Jedi object at 0x7f910c9d9390>
# If you run the same code on your computer, you'll see something very similar, although t
# he hexadecimal number (the substring starting with 0x) will be different.

# To get a result different from the default string above, the __str__() method would need to be defined in the Jedi class.