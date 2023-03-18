#!/usr/bin/python3
l1 = []
for x in range(5):
    l1.append(1 if x**2 % 2 == 0 else 0)

print(l1)