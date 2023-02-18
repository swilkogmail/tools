#!/usr/bin/python3
# What is the expected output of the following snippet ?
class Jedi:
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return "I am Jedi " + self.name
 
class Sith:
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return "I am Sith " + self.name
 
class Padawan(Jedi,Sith):
    def __init__(self,name):
        self.name = name
 
Baby_Yoda = Padawan('Baby Yoda')
print(Baby_Yoda)

# Explanation:
# Class Padawan is a subclass of both the Jedi and Sith classes. As such, all 
# methods defined in the superclasses  Jedi and Sithare automatically inherited by subclass Padawan.
# In particular, method __str__() is inherited by  subclass Padawan. This method 
# allows to customize the returned string when printing an object. But the __str__() 
# method is defined in both the  Jedi and Sith classes : so which one would be used when calling print(Baby_Yoda)  ?
# Python scans the inheritance path from left to right and will use the first __str__()  method 
# ound in one of the superclass : in the above case,  class Jedi is the first class with the __str__()  
# method in the Padawan inheritance path : so this is this method that will be used. If the  class P
# adawan had been defined as class Padawan(Sith,Jedi):  then the __str__() method from the Sith class would have been used.