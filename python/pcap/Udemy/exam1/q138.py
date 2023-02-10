#!/usr/bin/python3
# What is the expected output of the following code ?

class Jedi:
    LightSaber = 1
    def __init__(self):
        self.force = 10
        
 
class Sith(Jedi):
    def __init__(self): # the __init__() method of the Padawan class, the call to super().__init__() 
                        # is which is the Sith class, and defines property force as self.force = 15.
        self.force = 15
        
class Padawan(Sith):
    force = 5
    def __init__(self):
        super().__init__() # The super() builtin returns a proxy object (temporary object of the superclass) that allows to access methods of the base class.
                           # So, in the __init__() method of the Padawan class, the call to super().__init__() is
                           # the call to the __init__() method of the superclass of Padawan, 
                           # which is the Sith class, and defines property force as self.force = 15.
                           # So, Luke.force returns 15.
        
Luke = Padawan()
 
print(hasattr(Padawan, 'LightSaber')) # The hasattr() function allows to check if any object or class contains a specified property.
                                      # The first argument is the class of the object being checked, the second argument is the name of the property.
                                      # The function can also be used to find out if a class variable is available.
                                      # Luke is an object from class Padawan, which is a subclass from 
                                      # Sith which itself is a subclass from Jedi - in other words, the Padawan class 
                                      # inherits methods and properties from the Sith class and the Jedi class.
                                      # LightSaber is a class variable of the Jedi class and the Padawan class inherits it.


print(Luke.force) 