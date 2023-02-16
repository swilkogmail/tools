#!/usr/bin/python3
from vehicle import Vehicle
from bicycle import Bicycle

# __bases__ gives you the base classes
print(Vehicle.__bases__)
print(Bicycle.__bases__)

# this will return a list of subclasses that have been loaded from the class Vehicle
# i.e. it needs to have been imported above
print(Vehicle.__subclasses__())

# identifiers that can be chained off, __bases__ is not in there
print(dir(Bicycle))

# identifiers that can be chained off, __bases__ is not in there
print(hasattr(Bicycle,'boat type'))
print(hasattr(Bicycle,'default_tyre'))
# import to note that if you create an object it may have return true as it may create an
# attribute for the object that is not on the class, i.e. when bike is created it gets the
# attribute tyre, the class itself doesn't though
print(hasattr(Bicycle,'tyres'))
bike = Bicycle()
print(hasattr(bike,'tyres'))

print(issubclass(Bicycle, Vehicle))
# true
print(issubclass(Vehicle, Bicycle))
# false
# is subclass will look down the whole hierarchy and find out if that class is a class of another

# print(issubclass(bike, Vehicle)) # an error as bike is an instance of Bicycle
print(isinstance(bike, Vehicle))
# true as bike is an instance of Vehicle
print(isinstance(bike, Bicycle))
# true as bike is an instance of Bicycle

# this is the class that is used to intantiate the object
print(type(bike))

# all of the custom attributes
print(bike.__dict__)

# formatting object prints for debugging
# prior to adding __str__ in the Bicycle class it would print:
# <bicycle.Bicycle object at 0x7fccadc72fd0>
# Adding this:
    # def __str__(self):
    #     return f"<{self.__class__.__name__} {self.__dict__}>"
# results in 
print(str(bike))
# <Bicycle {'distance_traveled': 0, 'unit': 'miles', 'tyres': ['tyre', 'tyre']}>



    def __str__(self):
        return f"<{self.__class__.__name__} {self.__dict__}>"