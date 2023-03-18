#!/usr/bin/python3
# Which following statement is true (pick two) ?

# Explanation:

# ->" lambda  is a correct variable name." : this is false as lambda is a Python reserved keyword and cannot be used to name a variable.

# ->" _lambda  is a correct variable name." : this is true : a variable name can start with an underscore.

# ->" 1lambda  is a correct variable name." : this is false : a variable name cannot start with a number.

# ->" Lambda  is a correct variable name." : this is true.  Lambda (note the upper-case "L") is different from lambda (lower-case "l") which is a Python reserved keyword.

#lambda = 5     # SyntaxError
#print(lambda)
 
_lambda = 4     # OK
print(_lambda)  # 4
 
#1lambda = 3     # SyntaxError
#print(_lambda)  
 
Lambda = 8      # OK
print(Lambda)   # 8