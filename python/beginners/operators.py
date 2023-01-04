#!/usr/bin/python3
'''
unary operator only has 1 operator, '+' for example has two, i.e. 1 + 1 (the 1 and 1 are the operators)
~ only has one
e.g. ~1 
'''
# Bitwise complement operator
a = 0b010 # binary integer which in decimal is 2
print(bin(a))
b = ~a
print(b)
# ~ gives a way of showing a negative number the formla is -ve a - 1, i.e. -2 - 1 = -3
print(bin(~a))

#  AND OR XOR AND NOT

a = 0b1001
b = 0b1100
# | means OR either OR so if either of them is true then the resulting column is true (1 is true and 0 is false)
print(bin(a | b))
# AND & requires that both are true to return true
print(bin(a & b))
# XOR exclusive OR means on 1 true value should be there otherwise it's false
print(bin(a ^ b)) # NB it removed the trailing 0 so instead of 0b0101 it will be 0b101

# shift operators
a = 0b110
print(bin(a >> 2))  # shift the point two to the left
print(bin(a << 2))  # shift the point two to the left

'''
binary operations, more useful
not True
not False
or
and
'''
'''
Comparison
< less > greater <= >= # can be used to compare strings (place in alphabet)
== for equality, supports all types
!= for not equal
1 is 1 (is the identity operator)
1 is 1.0 (false)
'a' is 'a' (true)

is with list return fale if not initialised
i.e.
[] is []
false
that as empty list can be changed

id function can be used to return the immutable numer associated with a charater
ord function can be used to get the numeric value of a charcter

order of operators priority
https://docs.python.org/3/reference/expressions.html#operator-precedence

'''
print(ord('a'))
print(ord('A'))
print(id('A'))