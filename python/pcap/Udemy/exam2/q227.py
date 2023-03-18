#!/usr/bin/python3
# What is the expected output of the following snippet ?
x = 5//2
func = lambda x:+3 # x is a vaiable local to the lambda function so the definition outside of this o
                   # on the line above is out of scope therefore func will always return 3
print(func(x))