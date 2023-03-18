#!/usr/bin/python3
# You want to print the content of a text file named myfile.txt to the screen.
# Assuming the file exists and includes 10 lines of text (each line containing less than 10 characters), which code snippet can produce the expected result ?

# Explanation:
# readline(number) is used to read a single line from a text file; number is 
# optional : this is the maximum number of characters/bytes to read from the line.  If number  
# is omitted the whole line is read. Note that readline() returns a string.
# readlines(number) is used to read the lines from a text file; number is optional : If the 
# number of bytes returned exceed this number, no more lines will be returned. If number is 
# omitted, all lines are read. Note that readlines() returns a list of strings, one element per file line.
# read(number) is used to read the number characters/bytes from a file and returns them as a string - if number  is omitted the whole file is read.
# Here the only answer that would fulfill the requirements is :

f = open('myfile.txt', 'r')
data = f.read()
for x in data:
    print(x, end='')
f.close()