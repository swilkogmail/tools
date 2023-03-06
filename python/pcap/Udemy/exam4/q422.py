#!/usr/bin/python3
# Consider the code below :

class Alpha:
    def __init__(self, val):
        self.a = val
 
class Beta(Alpha):
    # insert code here
 
 
b = Beta(5,5)
print(b.a, b.b)

# What code do you need to insert (in the class Beta definition), so that the output of the above code is:

5 6

# Explanation:

# super() returns a reference to the nearest superclass of the class. When used within a constructor, there is no need to pass the self argument to the method being invoked. So, in the above answer, super().__init__(x)  will correctly invoke the Alpha constructor. An alternative would have been using the name of the super class explicitly as :

# Alpha.__init__(self, x)  (in this case the self argument must be passed to the constructor).

# Finally, to get 6 when printing b.b, we must have the following property definition in the Beta constructor :

# self.b = y + 1.