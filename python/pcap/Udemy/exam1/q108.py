#!/usr/bin/python3
# What will be printed to the monitor ?

w = 'Luke'
x = 'luke'
y = 10
z = 5
# print(w < x)
# print(x > y)
print(y < z)
# print(w > z)
# print(w < x and y < z)
# print(x > y and w > z)

# w < x True # code points of upper-case characters (A..Z) are less than code points of lower-case characters (a..z)
#             # 'Luke' < 'luke'   is True  ( upper-case 'L'  has a smaller code point than lower-case 'l' )
# y < z True # '10' < '5'   is True ('1' has a smaller code point than  '5' ) - note - these are strings

# false + false = True

# x > y true # 'luke' > '10'   is True  ( lower-case 'l'  has a greater code point than '1' )
# w > z true # 'Luke' > '5'   is True (upper-case 'L' has a greater code point than '5' )


# -> when comparing strings, Python compares code point values, character by character.

# -> string comparison is case-sensitive : upper-case letters are taken as lesser than lower-case

# -> when comparing two strings of different lengths and the shorter one is identical 
# to the longer one's beginning, the longer string is considered greater.

# -> when comparing a string to a number (integer or float), the only comparisons you 
# can perform are with the operators  == and != operators - other comparison operators (>, <) will raise an exception.

# -> code points of number characters (0..9) are less than code points of upper-case characters (A..Z)

# -> code points of upper-case characters (A..Z) are less than code points of lower-case characters (a..z)

# Note : function ord()  returns the code point of a given character.

# So, in the above question :

# 'Luke' < 'luke'   is True  ( upper-case 'L'  has a smaller code point than lower-case 'l' )

# '10' < '5'   is True ('1' has a smaller code point than  '5' )

# So : print('Luke' < 'luke' and '10' < '5')  will return True

# 'luke' > '10'   is True  ( lower-case 'l'  has a greater code point than '1' )

# 'Luke' > '5'   is True (upper-case 'L' has a greater code point than '5' )

# So : print('luke' > '10' and 'Luke' > '5')  will return True