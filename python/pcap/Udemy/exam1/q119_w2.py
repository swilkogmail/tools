#!/usr/bin/python3
# Consider the code snippet below:

class Snake:                    # line 1
    count = 0                   # line 2
    def __init__(self, val):    # line 3
        self.__count = val      # The property count from the object my_snake is defined in the constructor of the Snake class (__init__()) as : self.__count = val
        count=2                 # line 5
                                # line 6
class Python(Snake):            # Python is a type of snake
    def __init__(self, val):    # and its constructor
        super().__init__(val)   # is inherited from the supertypes constrctor
                                # line 10
my_snake = Python(1)            # line 11
print(my_snake._Snake__count)   # Answer inserted
# What code do you need to insert in line 12 to get the value of the property count from the object my_snake printed on the screen ?

# A:
# print(my_snake._Snake__count)

# Explanation:

# The property count from the object my_snake is defined in the constructor of the Snake class (__init__()) as : self.__count = val
# The __ (two underscores) preceding the name of the variable means that it is treated as a private instance variable. To access 
# such a private instance variable from outside the class, you need to use the "name mangling" convention, 
# i.e MyObject._MyClass__MyProperty where MyObject is the object from which you want to access 
# the property MyProperty  and MyClass is the class where the property is defined.
# MyObject = my_snake
# MyClass = _Snake
# MyProperty = __count
# So, to access the value of the property count from the object my_snake, you need to refer to variable my_snake._Snake__count.

class Snake:                    # line 1
    count = 0                   # line 2
    def __init__(self, val):    # line 3
        self.count = val      # The property count from the object my_snake is defined in the constructor of the Snake class (__init__()) as : self.__count = val
        count=2                 # line 5
                                # line 6
class Python(Snake):            # Python is a type of snake
    def __init__(self, val):    # and its constructor
        super().__init__(val)   # is inherited from the supertypes constrctor
                                # line 10
my_snake = Python(2)            # line 11
print(my_snake.count)           # if it wasn't a private instance variable then we can access it straight from the type that we have created