#!/usr/bin/python3
# Which code snippet would you replace zzz with to get 4 stars printed to the monitor ?

x = 1
while x < 10:
    print('*')


    # x *= 2*x

# 1st time x = 1 #print *
# 2nd x = 2 * (1x2)  which is 2 #print *
# 3rd x = 2 * (2x4)  which is 8 #print 8 and exit

# Explanation:

# you have to know about bitwise operators to answer this question correctly.

# >> and << are "shift operators". These operators are used to shift the bits of a number left or right thereby multiplying or dividing the number by two respectively. They can be used when we have to multiply or divide a number by two.

# Bitwise right shift ( >>): Shifts the bits of the number to the right and fills 0 on voids left( fills 1 in the case of a negative number) as a result. Similar effect as of dividing the number with some power of two.

# Example:
# a = 10 = 0000 1010 (Binary)
# a >> 1 = 0000 0101 = 5
# Bitwise left shift ( << ) : Shifts the bits of the number to the left and fills 0 on voids right as a result. Similar effect as of multiplying the number with some power of two.

# Example :
# a = 5 = 0000 0101 (Binary)
# a << 1 = 0000 1010 = 10
# a << 2 = 0001 0100 = 20 
# So,  x = x << 1  is equivalent to x = 2 * x  --> this would print 4 stars (for x=1, x =2, x=4 and x =8)

# and:   x = x >> 1  is equivalent to x = x /2 --> this would print an infinity of stars since the condition x < 10 would remain True at each iteration.

# += and *= are shortcut operators.

# x+=1   is equivalent to  x = x + 1  --> this would print 9 stars (for x=1,2,3,4,5,6,7,8 and 9)

# x *= 2*x   is equivalent to  x = x * (2*x)  --> this would print 3 stars (for x=1, 2 and 8)

Try it yourself:

x = 1
while x < 10:
    print('*')      # print 4 stars
    x = x << 1
    
print('--------')
 
x = 1
while x < 10:
    print('*')      # print 9 stars
    x+=1
    
print('--------')
 
#x = 1
#while x < 10:
#    print('*')     # infinite loop
#    x = x >> 1
    
print('--------')
 
x = 1
while x < 10:
    print('*')      # print 3 stars 
    x *= 2*x