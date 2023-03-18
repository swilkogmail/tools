#!/usr/bin/python3
# You want to read the content of file Stars.txt file and retrieve its first five lines.
# You started writing the following Python snippet:

f = open('Stars.txt','rt')    # Line 1 
# insert code here            # Line 2
f.close()                     # Line 3

# Explanation:
# readline(number) is used to read a single line from a text file; number is optional : 
# this is the maximum number of characters/bytes to read from the line.  If number  is omitted the whole line is read.
# readlines(number) is used to read the lines from a text file; number is optional : If the 
# number of bytes returned exceed this number, no more lines will be returned. If number is omitted, all lines are read.
# read(number) is used to read the number characters/bytes from a file and returns them as a string - if number  is omitted the whole file is read.
# Now, let's review the suggested answers:
# data = f.readlines(5)  would only read the first line since the first line has more than 5 characters 
# (and no more lines will be returned because of the maximum bytes parameter 5)
# data = f.readline(5)  would only read the first 5 characters of the first line.
# data = f.read(5)  would only read the first 5 characters of the whole file.
# data = f.readlines()[:5]   This will read all lines from the file and then slice the resulting list to its first 5 elements, which is what we need here.