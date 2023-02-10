#!/usr/bin/python3
# Two classes are defined as below :

class Jedi:
    def __init__(self, name):
        self.name=name
 
class Sith:
    def __init__(self, name):
        self.name=name
        
 
print(issubclass(Jedi, Sith))        # False
 
 
class Padawan(Jedi):
    def __init__(self, name):
        self.name=name
 
print(issubclass(Padawan, Jedi))     # True

# Which function would you use to check if Jedi is a subclass of Sith ?
# The function issubclass() is able to determine if Class_1 is a subclass of Class_2 :
# issubclass(Class_1, Class_2)  will return True if Class_1 is a subclass of Class_2 and False otherwise.
# The function isinstance() checks if an object comes from an indicated class:
# isinstance(Object, Class) will return True if Object comes from class  Class and False otherwise.