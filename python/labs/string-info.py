#!/usr/bin/python3
import math
string = input('Enter a string: ')
print(string)
print(string[0], "is the first character")
print(string[-1], "is the last character")

if len(string) % 2: # the string is odd
    print("The string has an odd number of characters")
    lower_mid = math.floor(len(string)/2)
    upper_mid = math.ceil(len(string)/2)
    print(lower_mid, "is the lower middle of the string")
    print(upper_mid, "is the upper middle of the string")
    print(string[lower_mid:upper_mid], "is the middle character")
else:
    print("The string has an even number of characters")
    lower_mid = int((len(string)/2)-1)
    upper_mid = int((len(string)/2)+1)
    print(lower_mid, "is the lower middle of the string")
    print(upper_mid, "is the upper middle of the string")
    print(string[lower_mid:upper_mid], "are the middle characters")

print(string[0::2], "even indexed")
print(string[1::2], "odd indexed")
print(string[::-1], "string in reverse")
