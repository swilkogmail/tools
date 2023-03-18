#!/usr/bin/python3

# Knowing that ord('a') has a value of  97, which code below will print bee to the monitor ?

# Explanation:

# Function ord() returns the Unicode code of a given character.

# Function chr() returns the corresponding character from a given Unicode code.

# The Unicode code of a is given in the question (you don't have to remember this for the 
# test !) : 97.  We can easily deduct the Unicode code of characters b and e :

# a --> 97

# b --> 98

# c --> 99

# d --> 100

# e --> 101

# Now, let's review each suggested answers:

--> print(chr(98) + 2*chr(101))

# This is equivalent to print('b' + 2*'e') , which will print bee (+ concatenates string and * repeats a string)

--> print(chr(ord('a')+1), chr(ord('a') + 4), chr(ord('a') + 4))

# This is equivalent to print('b', 'e', 'e')  which will print b e e (notice the space between the characters).

--> print(chr(98), chr(101), chr(101), sep=',')

# This is equivalent to print('b', 'e', 'e', sep=',')  which will print b,e,e (notice the comma between the characters).

--> print(''.join([str(ord('b')), str(ord('e')), str(ord('e'))]))

# This is equivalent to print(''.join(['98', '101', '101']))  which will print string 98101101.