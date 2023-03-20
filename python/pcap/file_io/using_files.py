#!/usr/bin/python3
# file_object.read()
# file_object.write()

# open('some_file.txt','w') w will truncate the file ready to start to write
# open('some_file.txt','r+')
# open('some_file.txt','a') # open for append
# +t is text +b is binary
# open('some_file.txt','r+t')

# open a file truncate it or create it if it doesn't exist and read from it
my_file = open('report.txt','w+')
my_file.write('line 1\n')
my_file.write('line 2\n')
# or write lines
my_file.writelines([
    'line 3\n',
    'line 4\n',
    'line 5\n'])

my_file.seek(0) # moves the cursor to the head of the file
print(my_file.read())
my_file.close()

my_file = open('report.txt','r')
print(my_file.read())
my_file.close()

# use the with statement to automatically close the file
my_file = open('report.txt','r')
with my_file:
    print(my_file.read())