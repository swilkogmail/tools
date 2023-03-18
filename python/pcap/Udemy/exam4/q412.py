#!/usr/bin/python3
# What is the expected output of the following code, assuming the user enters RAT when prompted with "Enter a password:" ?

pwd=input("Enter a password:")
 
if pwd.isalpha():
    pwd[-1]="A"
    print(pwd) 
elif pwd.isalnum():
    pwd[-1]="N"
    print(pwd)
else:
    print("Password must be alphanumeric.")

# Explanation:
# Python strings cannot be changed — they are immutable. Therefore, assigning to an indexed position in the string results in an error.
# Line of code pwd[-1]="A" will raise an unhandled exception.
# To avoid this, a new string should be created.
# Try it yourself:
# pwd=input("Enter a password:")
 
# if pwd.isalpha():
#     pwd[-1]="A"    # TypeError: 'str' object does not support item assignment
#     print(pwd)
# elif pwd.isalnum():
#     pwd[-1]="N"
#     print(pwd)
# else:
#     print("Password must be alphanumeric.")