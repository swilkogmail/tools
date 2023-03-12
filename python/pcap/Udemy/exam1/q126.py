#!/usr/bin/python3
# Question 17: Incorrect
# You want to print the content of a text file named myfile.txt to the screen.

# Assuming the file exists and includes 10 lines of text (each line containing less than 10 characters), which code snippet can produce the expected result ?

try:
    f = open('myfile.txt', 'wt')
    for i in range(10):
        s = "line #" + str(i+1) + "\n"
        f.write(s)
    f.close()
except:
    print("I/O error occurred:")
# End of code
 
# Now this part of the code is to read data from the file myfile.txt and print its content 
### answer #1  ###                                      
for line in open("myfile.txt", "rt"):
    print(line, end='')        # This will print the whole file as required                                
 
### answer #2  ### 
f = open('myfile.txt', 'rt')
data = f.readline()             
print(data)                    # This will only print the first line of the file 
f.close()
 
### answer #3  ### 
f = open('myfile.txt', 'r')
data = f.read()
for x in data:
    print(x, end='')           # This will print the whole file as required
f.close()
 
### answer #4  ### 
f = open('myfile.txt', 'r')
data = f.readlines(10)
print(data)                    # ['line #1\n', 'line #2\n']
f.close()


# Explanation:

# readline(number) is used to read a single line from a text file; number is optional : this is the 
# maximum number of characters/bytes to read from the line.  If number  is omitted the whole line is read. 
# Note that readline() returns a string.

# readlines(number) is used to read the lines from a text file; number is optional : If the number 
# of bytes returned exceed this number, no more lines will be returned. If number is omitted, all lines 
# are read. Note that readlines() returns a list of strings, one element per file line.

# read(number) is used to read the number characters/bytes from a file and returns them as a string - 
# if number  is omitted the whole file is read.

# Now, let's review the suggested answers:

# 1/ This would work

# 2/ This would only print the first line of the file

# 3/ This would work

# 4/ This would only print a few lines from the file, as a list. Exact number of lines would depend on 
# the number of characters in each line - Indeed,  f.readlines(10) would stop processing any new lines 
# after the 10 first bytes have been read.

# Please refer to the Try it Yourself section to see how those 4 answers work.

