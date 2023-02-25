#!/usr/bin/python3
# Consider the code below :
class Alpha:                    # line 1
    def __init__(self, val):    # line 2
        self.a = val            # line 3
                                # line 4
class Beta(Alpha):              # line 5
    #insert code here           # line 6
                                # line 7
beta = Beta("beta")             # line 8
print(beta)                     # line 9
# Which code snippet would you insert in line 6 so the above code produce the following output :
# I am beta, son of Alpha

# Explanation:
# __str__() is a method that allows to customize the string returned when printing an object.
# The expected output includes the name of the object being printed (in this case beta) 
# and the name of its superclass (Apha in this case).
# For object beta, beta.a returns string beta - so  self.a should be included in the __str__()  method.
# String Alpha, can be returned using the property __bases__ which is a tuple 
# that includes the direct superclasses of a class. The first (and only) element in 
# this tuple for class Beta is the class Alpha. Property __name__ will return the name of a class. So : Beta.__bases__[0].__name__  will return string Alpha.
# So, the correct answer is :
# def __str__(self):
#     return "I am " + self.a + ", son of " + Beta.__bases__[0].__name__  
# The three other suggested answers will raise an exception.
# Try it yourself:
class Alpha:                    
    def __init__(self, val):
        self.a = val   
 
class Beta(Alpha): 
    def __str__(self):
        return "I am " + self.a + ", son of " + Beta.__bases__[0].__name__   
 
beta = Beta("beta")
print(beta)         # I am beta, son of Alpha