#!/usr/bin/python3
# What is the expected output of the following code ?

class Class1:
    def __init__(self):
        self.a = 4
 
    def set(self):
        self.a += 1
        return self.a
 
class Class2(Class1):
    def set(self):
        self.a += 2
        return self.a
 
c=Class2()
print(c.set())

# class2 hasn't got a constructor so it uses the constructor of its supertype class1
# this inialises a as 4
# then the set function is called which class2 has locally so it doesnt go to the super type
# it raises a (set to 4) up 2 to 6. 

# Explanation:

# Class2 is a subclass of Class1 and, as such, inherits its methods and properties, including its constructor.

# So, when c is instantiated as an object of Class2, the instance variable  c.a has a value of 4.

# Method set() is defined in both Class2 and Class1 - so set() from Class2 overrides set() from Class1.

# So, when c.set() is invoked, instance variable  c.a is incremented by 2, and 6 is printed.