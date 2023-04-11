#!/usr/bin/env python3
x = 1

def func():
    x = 4 
    print(x)


func() # prints the val of x inside the func, i.e. 4
print(x) # prints 1

def func2():
    global x
    x = 4
    print(x)

func2() # prints and change the value of x global - 4
print(x) # 4
