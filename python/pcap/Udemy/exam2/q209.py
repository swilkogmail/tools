#!/usr/bin/python3
# What is the expected output of the following code snippet ?

# my attempt

class A:
    def __init__(self, x=5): # called from B wth x equal to 2
        self.x = x # x = 2
 
class B(A):
    def __init__(self, y=2):
        super().__init__(y) # initialise y with a default of 2 and call init from the super with 2
    def set(self, y): # y is called with arg x which is 2
        self.x = y + 3 # x is 2 + 3 which returns 5
        return self.x
 
b = B()
print(b.set(b.x + 2))


# correct answer:

class A:
    def __init__(self, x=5): # 
        self.x = x # So, after object b is created, b.x has a value of 2. set is invoked with 4 though
 
class B(A):
    def __init__(self, y=2):
        super().__init__(y) # B's constructor calls its direct superclass's constructor via line super().__init__(y)
    def set(self, y): # y is called with arg x which is 4
        self.x = y + 3 # x is 4 + 3 which returns 7
        return self.x
 
b = B() # b is an object from class B, which is a subclass of class A.
print(b.set(b.x + 2)) # call to b.set(b.x + 2)  is equivalent to b.set(4)

