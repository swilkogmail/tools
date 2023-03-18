#!/usr/bin/python3
# What is the output of the following code ?

class H:
    def __init__(self,x=0):
        self.h = x
    def set(self):
        self.h +=1
 
h1=H(1)
# h = 1
h2=h1
# h = 1
h2.set()
# h = 2
h1.set()
# h = 3
print(h2.h)
# 3

# Explanation:

# Objects are mutable - with the assignment h2=h1  both variables h2 and h1 point to the same object.

# So, h2.set() will increment h2.h and h1.h by 1.

# Same with  h1.set() which will increment h2.h and h1.h by 1.

# So, print(h2.h)  will print 3 to the screen.