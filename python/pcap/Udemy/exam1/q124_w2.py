#!/usr/bin/python3
# You want to create a new class Class2, as a subclass of class Class1.
# You want the constructor of Class2  to be exactly the same as the one from Class1 (this constructor has two parameters : self and val).
# Which code snippet below would comply with the above requirements ?
# answer:
# class Class2(Class1):
#     pass
# # With this code snippet, Class2 will inherit the constructor (and any other methods) of Class1 as-is.
# # An alternative to this answer could have been:
# class Class2(Class1):
#     def __init__(self, val):
#         Class1.__init__(self, val)
# # OR:
# class Class2(Class1):
#     def __init__(self, val):
#         super().__init__(val) 
# As a reminder, a constructor is a method in a class that will be invoked 
# automatically and implicitly when the object of the class is instantiated. This method is created as  __init__.

class Class1():
    def __init__(self, val):
        self.value = val

class Class2(Class1):
    pass

my_object1 = Class1(3)
print(my_object1.value)        # 3

my_object2 = Class2(3)
print(my_object2.value)        # 3