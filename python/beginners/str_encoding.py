#!/usr/bin/python3
# code points
# strings are stored in UTF8, unicode 8 bytes
print(ord('a'))
print(ord('£'))
# first alphabet characters are the same ascii and utf8
# code point for UTF8 is usually written in Hex formar, i.e. U+2122
# this will print the codepoint
print(0x2122)
# 8482
# shorthand using ord and UTF8 hex notation
print(ord('\u2122'))
print('\u2122') # prints out the actual symbol
# to take the character (codepoint) values and convert to string we can use
print(chr(8482))