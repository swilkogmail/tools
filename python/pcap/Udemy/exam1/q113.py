#!/usr/bin/python3
# What is the expected output of the following code?

def my_func(x,y):
    return x / y
 
try:
    my_func(5,0)
except ArithmeticError:
    print("A")
except ZeroDivisionError:
    print("B")
else:
    print("C")
finally:
    print("D")

# Explanation:

# my_func(5,0)  will raise an exception (can't divide 5 by 0). Since this statement is in a try:  
# clause, one of the except clause will be executed ; which one ? This will depend on the type of 
# exception and the order of the except clauses.

# 5/0  would raise a ZeroDivisionError exception, which is the second except clause. But the first 
# except clause is for ArithmeticError  exceptions which is a superclass of ZeroDivisionError - so 
# the except ArithmeticError: clause would be the first one matching the exception raised by my_func(5,0)  and would print the letter A.

# The else: clause would not be executed (since one of the except clause was executed).

# And the finally: clause is always executed : so letter D will be printed.