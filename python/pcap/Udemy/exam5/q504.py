#!/usr/bin/python3
# What value will be printed to the monitor ?
z = 3
y = 7
x = y == z and y > z or z > y and z != y  # x is the result of the Boolean expression y == z and y > z or z > y and z != y
print(int(x))

# so it's (y == z and y > z) or (z > y and z != y)
# false and true which is false
# false and true which is false
# false or flase which is false
# when true is converted to an integer it's 1
# when flase is converted to an integer it's 0
# answer is 0

LOGICAL OPERATOR AND HAS PRESENDENCE OVER or

# So expression A = y == z and y > z gets evaluated first.
# Then expression B = z > y and z != y gets evaluated second.
# Finally expression A or B gets evaluated last.



# Explanation:

# x is the result of the Boolean expression y == z and y > z or z > y and z != y

# To correctly evaluate this expression you have to remember that logical operator and has precedence over logical operator or.

# So expression A = y == z and y > z gets evaluated first.

# Then expression B = z > y and z != y gets evaluated second.

# Finally expression A or B gets evaluated last.

# y == z  is False

# y > z  is True

# So,  y == z and y > z   is equivalent to  False and True  which is False

# z > y  is False

# z != y is True

# So,  z > y and z != y   is equivalent to  False and True  which is False

# Finally, False or False   is False.

# The int() function will convert the input  to an integer. When the input is a Boolean :

# int(False)   returns 0.

# int(True)  returns 1.