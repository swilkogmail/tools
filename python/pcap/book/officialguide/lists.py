#!/usr/bin/env python3
x = [0,1,2]
print(x)
x.insert(0,1) # insert will insert an item at a given position
              # insert 1 at the zeroith position
print(x)
# list is [1,0,1,2]
del x[1]
print(x)
# list is [1,1,2]
print(sum(x))
# 4