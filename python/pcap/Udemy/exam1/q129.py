#!/usr/bin/python3
# What is the expected output of the following code snippet ?

class Sith:
    darkside= True # - class variable will not appear in the __dict__ variable of an object.
    def __init__(self, x, y):
        self.name = x
        self.lightsaber = 1
        self.__son = y
    def __str__(self):
        return self.name
 
Vader = Sith("Vader", "Luke")
Vader.__daughter = 'Leia' # - private instance variable defined inside the class will appear in the dictionary using 
                          # "name mangling", i.e. : _className__variable where className is the name of the class where that private instance variable is defined.
                          # - private instance variable defined outside the class will appear in the dictionary as __variable
print(Vader.__dict__) # __dict__ is a predefined property of all Python objects : this variable is a dictionary 
                      # and contains the names and values of all the variables the object is currently carrying.

# Explanation:

# __dict__ is a predefined property of all Python objects : this variable is a dictionary 
# and contains the names and values of all the variables the object is currently carrying.

# A few things to remember about __dict__ for an object :

# - class variable will not appear in the __dict__ variable of an object.

# - private instance variable defined inside the class will appear in the dictionary using 
# "name mangling", i.e. : _className__variable where className is the name of the class where that private instance variable is defined.

# - private instance variable defined outside the class will appear in the dictionary as __variable

# Based on the above rules, the only correct answer is :

# {'name': 'Vader', 'lightsaber': 1, '_Sith__son': 'Luke', '__daughter': 'Leia'}
# (son is a private instance variable defined inside the class; daughter is a private instance variable 
# defined outside the class; variable darkside does not show up since it is a class variable).