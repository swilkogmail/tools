#!/usr/bin/python3
# What is the expected output of the following code ?
class Jedi:
    def __init__(self):
        self.force = 10
        
class Sith:
    def __init__(self):
        self.force = 15
        self.bases = 1
        
class Padawan(Sith, Jedi):
    def __init__(self):
        super().__init__()
 
Luke=Padawan()
# print(Luke.__bases__)
print(Padawan.__bases__)

# __bases__ is built-in property of a class. It is a tuple which contains classes which are direct superclasses for the class.

# Only classes have this attribute - objects don't.

# So print(Luke.__bases__)  where Luke is an object from class Padawan  is erroneous and will raise an exception.

# On the contrary, print(Padawan.__bases__)  will print the direct superclasses of class Padawan :

# (<class '__main__.Sith'>, <class '__main__.Jedi'>)
