#!/usr/bin/python3
# What is the expected output of the following code ?

class Feline:
    def __init__(self, f=1):
        self.f = +f # cat2.f was set to 3
        self.g = -f # cat2.f was set to -3
    def reset(self, f=2):
        self.f += f # cat2.f has now a value of 5
        return self.f
 
cat1 = Feline(2) 
print(cat1.f)
print(cat1.g)
cat2 = Feline(3)
cat1 = cat2 # both cat1 and cat2 variables points to the same object.  
            # cat1 now references the object cat2 and its variables ('f' and 'g').
cat2.reset() # cat2.reset()  will increment cat2.f  by 2
print(cat1.f)


# Explanation:
# An object is mutable : assigning an object B to another object A will have the variable representing object A referencing the object B.
# So, with line cat1 = cat2 , both cat1 and cat2 variables points to the same object.  cat1 now references the object cat2 and its variables ('f' and 'g').
# And any operation done on cat2.f is equivalent to performing an operation on cat1.f.
# cat2.reset()  will increment cat2.f  by 2 ; since cat2.f was set to 3 by the Feline's constructor, cat2.f has now a value of 5.  That's also the value of cat1.f.
# So, print(cat1.f)  returns 5.