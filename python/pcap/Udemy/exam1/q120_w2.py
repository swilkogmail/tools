#!/usr/bin/python3
# What is the expected output of the following code snippet ?

class AlphaDivisionError(ZeroDivisionError):	
    def __init__(self, message):
        ZeroDivisionError.__init__(self, message)
 
def func_div(x,y):
    if y==0:
        raise ZeroDivisionError("Can't divide by zero !")
    elif isinstance(y, str):		
        raise AlphaDivisionError("Can't divide by string !") # AlphaDivisionError is a self-defined exception and is defined as a sub-class of the ZeroDivisionError class.
    else:		
        return x/y
 
try:
    print(func_div(4,'a')) # In function func_div(), if the second argument is a string (i.e. isinstance(y, str) returns True), the AlphaDivisionError exception is raised.
except ZeroDivisionError as e:
    print(str(e))
except Exception as e:
    print("There is an error !")
else:
    print('All good !')

# Explanation:


# So :  print(func_div(4,'a')) will raise the AlphaDivisionError exception. The first  except:  branch that matches the 
# AlphaDivisionError exception is the branch except ZeroDivisionError as e:  since AlphaDivisionError  is a sub-class of ZeroDivisionError.

# Consequently, message Can't divide by string !  is printed out.
