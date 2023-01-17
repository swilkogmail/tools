#!/usr/bin/python3
my_string = 'hello world'
print(my_string.lower())
print(my_string.upper())
print(my_string.capitalize())
print(my_string.title())

# returns true if all charaters of the strings are in the ascii codepoint range
print(my_string.isascii())
print(my_string.islower())
print(my_string.isupper())
print(my_string.istitle())
print(" ".isspace())
# they can be chained together. i.e. return it title case and then check it
print(my_string.title().istitle())
# decimals and numbers
print('1.0'.isdecimal()) # is it written in decimal notation, doesn't work with floats
print('1'.isdecimal()) # needs to be a whole number in decimal notation
print('a'.isdecimal())
print('1'.isnumeric()) # works the same way - not with floats
print('ajhfsgdjhfgsrjh'.isalpha())
print('ajhfsgd6jhfgsrjh'.isalpha())
print('ajhfsgd6jhfgsrjh'.isalnum())
print('1bear'.isidentifier()) # can it be used as a variable
print('1bear'.isprintable())
print('1bear\n'.isprintable()) # false as maintains new line character
# work with strings as tokens
phrase = 'this:is:a:phrase'
words = phrase.split(':')
print(words)
print(words[3])