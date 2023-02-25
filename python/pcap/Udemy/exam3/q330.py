#!/usr/bin/python3
# What will be the output of the following code ?

class Tau:
    T = 0
    # T is a class variable from class Tau.
    def __init__(self, t=0):
        self.t=t
        # The constructor from class Tau will update the value of variable T (via line Tau.T += t).
        Tau.T += t
 
t1 = Tau()
# After the creation of object t1, T has a value of 0.
t2 = Tau(2)
# After the creation of object t2, T has a value of 2.
t3 = Tau(3)
# After the creation of object t3, T has a value of 2+3,  i.e. 5.
print(t1.T)

# So, the last line of the above code (print(t1.T) ) will return 5.