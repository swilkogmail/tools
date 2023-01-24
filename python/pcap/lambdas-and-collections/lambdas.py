#!/usr/bin/python3
def name(a,b):
    print("something")
    1 + a
    return b

# lambdas are single expression anaymous functions

def square(num):
    return num * num

square_lambda = lambda num: num * num

assert square(4) == square_lambda(4)


# working with collections and lambdas
# higher order fuctions can take a function as an argument or it will return a function

