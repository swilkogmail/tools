#!/usr/bin/python3
# What is the expected output of the following code?

x = 1
y = 2
z = x//y # z = 0
x, y, z = y, z, z  # x = 2 y = 0 z = 0
z, y, z = x, z, y  # z = 2 y = 0 z = 0
print(x, y, z)

