#!/usr/bin/python3
# when you created functions they can hold on to information
# from their parent scopes that are suually cleaned up
# usually other_name would be cleaned up although because of
# closure it is held on to
#

def greeter(prefix):
    other_name = prefix + "xxx"
    def greet(name):
        print(f"{prefix} {name} {other_name}")
    return greet

hello = greeter("Hello,") # return a function called hello
goodbye = greeter("Goodbye,")

hello("Kevin") # call the function that was returned with some a new arg - note that prefix is held on too and so is other_name
goodbye("Sam")
