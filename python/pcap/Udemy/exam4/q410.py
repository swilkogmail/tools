#!/usr/bin/python3
# What is the expected output of the following code if the user enters 133 when prompted with "Enter integer between 0 and 100 : " ?

class NotInRangeError(Exception):
    def __init__(self, val, message="Value is out of range"):
        self.val = val
        self.message = message
        super().__init__(self.message, self.val)
 
try:
    guess = int(input("Enter integer between 0 and 100: "))
    if not 0 <= guess <= 100:
        raise NotInRangeError(guess)
except Exception as ex:
    for arg in ex.args:
        print(arg, end=' ')


# Explanation:
# Because the user enters a value that is not in the range [0,100], the NotInRangeError 
# exception is raised. This is a custom exception, sub-class of the Exception 
# class, and with two properties that are passed to the constructor of its superclass.
# The args property is a tuple that contains all arguments passed to the class 
# constructor - in this case both the message and val properties of NotInRangeError are passed to the Exception constructor (in that order).
# The resulting output is : Value is out of range 133