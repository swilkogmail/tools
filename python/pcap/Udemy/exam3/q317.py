#!/usr/bin/python3
# what is the expected output of the following code?

def my_func(x,y):
    return (x+1) / (y-1)
 
try:
    my_func(3,1)
except IndexError:
    print("A")
except ValueError:
    print("B")
except ArithmeticError:
    print("C") # correct
except ZeroDivisionError:
    print("D")

# Explanation:
# my_func(3,1)  will return (3+1)/(1-1) i.e : 4/0 . This will raise an exception ZeroDivisionError.
# But if you inspect the different except branches defined in the question, you will notice 
# that the branch except ArithmeticError:  is placed before the branch except 
# ZeroDivisionError: - and ArithmeticError is a superclass of ZeroDivisionError.
# So, the except ArithmeticError:  is the one which will be executed and C will be printed out.
# In general, more concrete exceptions (like ZeroDivisionError) should be placed 
# before the more general exceptions (like ArithmeticError).