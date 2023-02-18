#!/usr/bin/python3
# You want to read the content of a file named Stars.bin.
# You started creating the Python code below:

data = bytearray(10)                # Line 1
                                    # Line 2
try:                                # Line 3
    f = open('Stars.bin', 'rb')     # Line 4 
    f.readinto(data)  # insert code here              # Line 5
    f.close()                       # Line 6                            
except:                             # Line 7
    print("I/O error occurred:")    # Line 8

# Explanation:
# readinto()  is the correct function to read a binary file into a byte array.
# readline(number) is used to read a single line from a text file; number is optional : 
# this is the maximum number of characters/bytes to read from the line.  If number  is omitted the whole line is read.
# readlines(number) is used to read the lines from a text file; number is optional : If the 
# number of bytes returned exceed this number, no more lines will be returned. If number is omitted, all lines are read.
# read(number) is used to read the number characters/bytes from a file and returns them as a string - i
# f number  is omitted the whole file is read. Although read() can also be used to read a binary file, 
# the usage as suggested in the above answer is not correct and would raise an exception.