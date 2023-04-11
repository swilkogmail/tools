#!/usr/bin/env python3

class Test:
    def __init__(self, id):
        self.id = id
        id = 100
        # id above is a local variable of this method


x = Test(23)

print(x.id)


print(x.__dict__)
print(Test.__dict__)
print(hasattr(x,'id'))
print(hasattr(Test,'id'))
