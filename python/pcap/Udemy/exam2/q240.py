#!/usr/bin/python3
# What is the expected output of the following code ?
class Omega:
    def __init__(self):
        self.set(3)
        # The Omega constructor calls the set() method - this method is defined in both classes Lambda and Omega - 
    def set(self, x):
        self.x = x//2  
    
    # Since L.x has a value of 2 , L.x/3 is 0.6666666666666666  (a float) and str(L.x/3) 
    # is the string 0.6666666666666666 - the last character of this string is 6.
 
class Lambda(Omega):
    L = 4
    def __init__(self):
        super().__init__() # The constructor for class Lambda calls the constructor of Omega (super().__init() is equivalent to Omega.__init__(self))
    # Because the Lambda class has a custom __str__() method defined, the result of print(L) 
    # will be whatever string is defined in Lambda's __str__() method    
    # str(self.x/3)[-1] will return the last character of the string str(self.x/3)
    def __str__(self):
        return str(self.x/3)[-1]  
        # str(self.x/3)[-1] will return the last character of the string str(self.x/3) . 
        # Since L.x has a value of 2 , L.x/3 is 0.6666666666666666  (a float) and str(L.x/3) is 
        # the string 0.6666666666666666 - the last character of this string is 6.   
    def set(self, x): 
        self.x = x//2 + 1
        # since object L is from class Lambda its method set() will override the set() method defined in class Omega .
        # So L.x has a value of 3//2 + 1 which is 2. 
 
L = Lambda() # L is an object of class Lambda which is a subclass of Omega.
print(L)

# Explanation:

# Because the Lambda class has a custom __str__() method defined, the result of print(L) will be whatever string is defined in Lambda's __str__() method.

# 'a//b' will divide a by 3 and return just the integer part 

