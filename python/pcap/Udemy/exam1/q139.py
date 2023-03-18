#!/usr/bin/python3
# What is the expected output of the following code ?
class Jedi:
    def __init__(self, name):
        self.name = name # name is one of the property from Luke and its value is 'Luke'  as per the Jedi class constructor --> 
                         # that's the first element of the dictionary : 'name': 'Luke'.
 
    def set_force(self, val):
        self.__force = val  # force is another property from Luke and is set to 10 as per the call to  Luke.set_force(10). 
                            # However, the force property has been defined privately (note the two underscores in front of force).  
                            # In that case, Python uses "name mangling" when accessing the property from outside the class : it puts 
                            # the class name before the property name and puts an additional underscore at the 
                            # beginning --> that's the second element of the dictionary : '_Jedi__force': 10.
 
Luke = Jedi('Luke')
Luke.set_force(10)
Luke.lightsaber = True # Finally, the Luke object has been enriched with a new property named lightsaber on the fly, 
                       # outside the class (which is permitted)  and set with a value of True  --> that's the third element of the dictionary : 'lightsaber': True.
 
print(Luke.__dict__)

# {'name': 'Luke', '_Jedi__force': 10, 'lightsaber': True}

# Explanation:

# __dict__ is predefined object variable which is a dictionary containing the names and values of all the properties (variables) the object is currently carrying.

# So Luke.__dict__ will return a dictionary of the properties (names and values) from object Luke.

# name is one of the property from Luke and its value is 'Luke'  as per the Jedi class constructor --> 
# that's the first element of the dictionary : 'name': 'Luke'.

# force is another property from Luke and is set to 10 as per the call to  Luke.set_force(10). 
# However, the force property has been defined privately (note the two underscores in front of force).  
# In that case, Python uses "name mangling" when accessing the property from outside the class : it puts 
# the class name before the property name and puts an additional underscore at the beginning --> that's the second element of the dictionary : '_Jedi__force': 10.

# Finally, the Luke object has been enriched with a new property named lightsaber on the fly, 
# outside the class (which is permitted)  and set with a value of True  --> that's the third element of the dictionary : 'lightsaber': True.

# All in all, print(Luke.__dict__) returns :

