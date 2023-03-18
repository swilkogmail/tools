#!/usr/bin/python3
# Assuming the variables x, y and z have been defined as follow :

x = 5%2 # 5%2 returns 1 . So x = 1 bool true
y = 2**0 # 2**0 returns 1 . So y =1 bool true
z = [False] # bool true
# Which of the following statements is true ?


# Explanation:

# 5%2 returns 1 . So x = 1

# 2**0 returns 1 . So y =1

# z is a list with one value (it does not matter if this value is the boolean False !) , so bool(z) is True.

# bool(1) returns True.

# so, bool(y) and bool(x)  is equivalent to True and True  which is True.

# and bool(y) == bool(x)  is equivalent to True == True  which is True.

# Finally, not bool(y)  is equivalent to not True which is False.