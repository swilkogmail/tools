#!/usr/bin/python3
# Consider the code snippet below :
class A:
    a=0
    def __init__(self, x, y):
        self.b = x
        self.c = y
 
class B(A):
    b = 0
    def __init__(self, x, y, k):
        super().__init__(x, y)
        if k % 2 == 0:
            self.e = k
 
 
c = B(2,5,7)
c.f = 4

# Explanation:
# issubclass() is a function which can be used to identify whether or not a class is a subclass of another class.
# The syntax is : issubclass(Class1, Class2)  (is Class1 subclass of Class2 ?) It will return True if Class1 is a subclass of Class2 and False otherwise.
# hasattr()  is a function which can be used to determine if an object or a class contains a specified property.
# The syntax is : hassttr(object, 'attribute')  (does object contains property  'attribute'  (attribute name as a string)). 
# It will return True if  that's the case - False otherwise.
# In the above question, only the following statements returns True:
# issubclass(B, A) (B is indeed a subclass of A)
# hasattr(c, 'c') ( object c does have an attribute 'c' - B's constructor includes super().__init__(x, y)  
# which will invoke the constructor for B's superclass (A) and will provide object c with attributes 'b' and 'c'.
# The other statements returns False:
# issubclass(A, B) : class A is not a subclass of B
# hasattr(c, 'e') : object c does not have an attribute 'e' - this is because of the condition if k % 2 == 0:  in the class B constructor.