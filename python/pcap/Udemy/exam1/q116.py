#!/usr/bin/python3
# What is the expected output of the snippet below:

class Jedi:
    Force = 0 # Jedi.Force is a class variable. 
    def __init__(self,name):
        Jedi.Force +=1 # It is incremented by one any time a new object from class Jedi is created (Jedi.Force +=1  in __init__() of Jedi class).
        self.name = name
    def __str__(self):
        return "I am master Jedi " + self.name

# The __str__()  method allows to customize the string that will be printed out when printing an object. 
# The Padawan class inherits the __str__() method defined in the Jedi class. 
# So print(Baby_Yoda) will return : I am master Jedi Baby Yoda 

class Padawan(Jedi):
    def print(self):
        return "I am a Padawan"
 
Luke=Jedi('Luke')
print(Jedi.Force)
Ben=Jedi('Ben')
print(Jedi.Force)
Baby_Yoda=Padawan('Baby Yoda') # Class variable Jedi.Force is also incremented by one any time a new object from class Padawan is created
print(Jedi.Force)
print(Baby_Yoda)

# Explanation:

# The Padawan class is a subclass of the Jedi class; as such the Padawan class automatically inherits the 
# instance and class variables as well as the methods of its superclass (Jedi). This is the basis of inheritance in Object-Oriented Programming.

# Jedi.Force is a class variable. It is incremented by one any time a new object from class Jedi 
# is created (Jedi.Force +=1  in __init__() of Jedi class).

# The Padawan  class inherits the same constructor defined in the Jedi class 
# (there is no constructor defined in the Padawan class so it is not overriding 
# the constructor from the Jedi class and directly inherits it). So class variable Jedi.Force is also incremented by one any time a new object from class Padawan is created.

# Since two objects from the Jedi class and one object from the Padawan class are created, print(Jedi.Force) will return 3.

# The __str__()  method allows to customize the string that will be printed out when printing an object. 
# The Padawan class inherits the __str__() method defined in the Jedi class. 
# So print(Baby_Yoda) will return : I am master Jedi Baby Yoda

# So, final answer is :

# 3
# I am master Jedi Baby Yoda 