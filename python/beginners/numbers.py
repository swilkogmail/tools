#!/usr/bin/python3
num = 1+1
flt = 1.0 + 1.0
big_num = 4.5e9


print(big_num)
print(num)
print(flt)

## operators

num1 = 5
num2 = 3

print(num1 + num2)
print(num1 / num2)
print(num1 * num2)
print(num2 / num1)
print(num2 // num1) # floor division - how many times it evenly divides
print(num2 % num1) # mod - returns the rem  any iteger using mod 2, i.e. num % 2 will return 0 if even 1 if odd
print(num1 ** num2)

"""
Binary number start with 0b Octal start with 0o and Hex start with 0x
base 2, 8 and 16
2 in binary is 10
8 in octal is 10
16 in Hex is 10 - hex count 1,2,3,4,5,6,7,8,9,A,B,C,D,E,F then 10-19,1A,1B,1C,1D,1E,1F etc..

converting decimal to binary e.g. using 15

15/2 => 7 w/remainder of 1 - least significant
then
7/2 => 3 w/remainder of 1
then
3/2 => 1 w/remainder of 1
then
1/2 => 0 w/remainder of 1, this is the end as we now have 0  - most significant

in terms of order of the number we work backwards

to convert back to decimal:

1111
(1*2 power 3)+(1*2 power 2)+(1*2 power 1)+(1*2 power 0)

8+4+2+1 = 15

"""