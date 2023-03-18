#!/usr/bin/python3
# Consider the code below :
import math            # Line 1
print(dir(math)) # insert code here     # Line 2
# Which code snippet would you replace line #2 with to get the following output ?

# ['__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 
# 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'copysign', 
# 'cos', 'cosh', 'degrees', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 
# 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 
# 'isfinite', 'isinf', 'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 
# 'modf', 'nan', 'pi', 'pow', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 
# 'tanh', 'tau', 'trunc']

# The dir(module) function returns an alphabetically sorted list containing 
# all entities' names available in the specified module.

# In the above question, the expected output is the sorted list of all 
# entities's names available in the math module. 
#
#  So print(dir(math)) will produce exactly the required output and is the correct answer.

# Let's review the other suggested answers:

# -> show(math)  This will raise an exception - there is no Python built-in function show().

print(math.__dict__) # This will print a dictionary containing the module’s entities' names and their descriptions.

print(math.__name__) # will print the name of the math module : math
