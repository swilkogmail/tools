#!/usr/bin/env python3
d = {}
d[1] = 1
# {1:1}
d['1'] = 2
# {1:1,'1':2}
d[1] += 1
# {1:2,'1':2}

sum = 0

for k in d: # values in dictionary
    sum +=  d[k] # 1 + 2

print(sum)
4
