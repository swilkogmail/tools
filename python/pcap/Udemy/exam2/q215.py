#!/usr/bin/python3
# What is the expected output of the following code ?

class Game:
    def __init__(self, val):
        if val %2 ==0 :
            self.__g = val
        self.G = val + 1
 
g= Game(4)
print(g.__g)

# create a new object called g - type Game
# g will contain 
    # 4 %2 = 0 therefore __g will be 4
    # G will be 5
# g.__g  is not correct but g._Game__g  is correct (name mangling).

# as __g is private to Game we have to reference it with the class name, i.e. g._Game__g  object._<class>__var