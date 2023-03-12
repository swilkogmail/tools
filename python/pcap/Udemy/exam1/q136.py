#!/usr/bin/python3
# What is the expected output of the following code (assuming file myfile.txt exists and is not empty) ?
f = open("myfile.txt", "r")
print(f.readline(20))

# The readline() method returns one line from the file. The optional parameter specifies 
# the number of bytes from the line to return (default -1, which means the whole line).