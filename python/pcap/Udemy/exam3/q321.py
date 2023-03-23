#!/usr/bin/python3
# Consider the code snippet below :

class Alpha:
    a=5
    def __init__(self, x):
        self.b = x
 
class Beta(Alpha):
    c = 2
    def __str__(self):
        return "Beta"
 
beta = Beta(5)
beta.d = 4

print(beta.__dict__)
print(Beta.__dict__)
print(Alpha.__dict__)

print(hasattr(beta,'a'))
print(hasattr(beta,'b'))
print(hasattr(beta,'c'))
print(hasattr(beta,'d'))


print(hasattr(Alpha,'a'))
print(hasattr(Alpha,'b'))
print(hasattr(Alpha,'c'))
print(hasattr(Alpha,'d'))

print(hasattr(Beta,'a'))
print(hasattr(Beta,'b'))
print(hasattr(Beta,'c'))
print(hasattr(Beta,'d'))

# --> issubclass(Alpha, Beta) : function issubclass(Class_1, Class_2) is able to 
# determine if Class_1 is a subclass of Class_2. Alpha is not a subclass of Beta 
# (Beta is a subclass of Alpha). So, this statement will return False .

# --> hasattr(beta, 'a') : hasattr() can be used to determine if any object/class 
# contains a specified property. Object beta does contains the property 'a' which 
# is a class variable and which beta has inherited as class Beta is a subclass of class Alpha.

# --> isinstance(Beta, Alpha)  : function isinstance(Object, Class) checks if an object 
# comes from an indicated class. Beta is a class, not an object and so isinstance(Beta, Alpha)  will return False.

# --> type(Beta.__bases__) is dict  : __bases__ is a property of a class which contains the 
# class's superclasses (not just their names but the actual superclasses). This property is a tuple, not a dictionary. So this statement will return False.