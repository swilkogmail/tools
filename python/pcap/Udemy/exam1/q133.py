#!/usr/bin/python3
# What is the expected output of the following code ?

class Robot:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return "My name is " + self.name

class Droid(Robot):
    # def __init__(self, name):
    #     super().__init__(name)
    def __str__(self):
        return "Hello I am a Droid and my name is " + self.name

# switch the comments in the above code to get the strings printed from
# class or supertype class

 
R2D2 = Droid("R2D2")
print(R2D2)

# Explanation:

# When a subclass defines a method/class variable/instance variable of the same name 
# as existing in the superclass, the new name overrides any of the previous instances of the name.

# In the above question, Droid is a subclass of Robot and overrides the __str__() method.

