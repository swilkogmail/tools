#!/usr/bin/python3
def outer(par):
    x = par

    def inner():
        return x
    
    return inner

y = 10
f = outer(y)
x = inner()
print(x)