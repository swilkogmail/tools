#!/usr/bin/python3
# What is the expected output of the following code?

x = chr(ord('A') + 1) > chr(ord('b') - 1)
print(x)


# Explanation:

# ord() function returns the Unicode code from a given character.

# For example, ord(‘A’) returns the integer 65.

# chr() function returns the character from a given Unicode code.

# For example, chr(66) returns the character B.

# So chr(ord('A') + 1) is equivalent to chr(65 + 1) which is B - which makes sense because the Unicode of B is the Unicode of A + 1.

# And chr(ord('b') -1) is the character with the Unicode of b -1 which is a.

# Finally, when comparing two characters with > or < , that's their Unicode code that is compared.

# You have to remember that all capital letters (A, B, C...Z) have a smaller Unicode code than lowercase letters (a,b,...z).

# So, the Unicode of B (66) is smaller than Unicode of a (97) and consequently :  x is False.