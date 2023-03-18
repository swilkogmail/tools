#!/usr/bin/python3
# You are writing a Python function and want to handle both ArithmeticError exceptions and LookupError exceptions under one single except branch.
# The function looks like this :

def my_fun(x,y):                    # line 1
    try:                            # line 2
        # my code for try branch    # line 3
    # catch exceptions here         # line 4
        # my code for except branch # line 5
    return None                     # line 6

# Explanation:
# It is possible to handle two exceptions (or more) exc1 and exc2  using the following syntax:
try:
    #<code>
except (exc1, exc2):
    
    #<code>
# So, the only correct answer is :
# except (ArithmeticError, LookupError):
# The other answers will trigger an error.
# Try it yourself:
try:
    raise ArithmeticError
except (ArithmeticError, LookupError):
    print("in the except branch")    # in the except branch
 
try:
    raise LookupError
except (ArithmeticError, LookupError):
    print("in the except branch")  # in the except branch
 
try:
    raise ArithmeticError
except ArithmeticError, LookupError: 
    print("in the except branch")  #SyntaxError
 
try:
    raise ArithmeticError
except [ArithmeticError, LookupError]:
    print("in the except branch")  # Error