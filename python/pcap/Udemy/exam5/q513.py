#!/usr/bin/python3
# What is the expected output of the following code?

x = range(3, 12, 3)
print(x)
print(sum(x))
for n in x:
  if (n%2 == 0):
      print(n, end='')  # 6 will be printed
  else:
      pass
else:
    print(sum(x)) # this prints the sum of the list which is 18

# so 6 is printed and 18 is
# 618



# Explanation:

# The range(start, stop, step) function creates a sequence (iterable) based on the following parameters:

# start (Optional) : An integer number specifying at which position to start. Default is 0

# stop (Required) : An integer number specifying at which position to stop (not included).

# step (Optional): An integer number specifying the incrementation. Default is 1

# so range(3,12,3) returns the following sequence : [3,6,9]

# Looping through this sequence, only 6 is even (n%2 == 0 is True when n=6), so only 6 gets printed to the screen.

# The else keyword in a for loop specifies a block of code to be executed when the loop is finished - in this case, print(sum(x))

# is executed : the sum() function adds the items of an iterable and returns the sum; in this case : sum([3,6,9]) returns 18.

# So the end result is : 618