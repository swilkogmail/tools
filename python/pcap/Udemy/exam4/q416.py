#!/usr/bin/python3
# Which of the following statement is True ?

# String comparison is done comparing Unicode code point values, character by character.
# String comparison is always case-sensitive : upper-case letters have a smaller Unicode code point than lower-case letters.
# Comparison (< or > ) between a string and a number (float, int) will raise an exception.
# Based on this, let's review each suggested answers:
# --> 'Mexico' > 'mexico'
upper case characters have smaller unicode value thank lowercase
# Unicode code point of character M is smaller than the code point of character m - so above statement is False.
# --> '3' > 2
# This will raise an exception.
# --> '12' < '4'
# Unicode code point of character 1 is smaller than the code point of character 4 - so above statement is True.
# --> str(10) > str(8)
# Unicode code point of character 1 is smaller than the code point of character 8 - so above statement is False.