#!/usr/bin/python3
# What is the expected output of the following code, assuming the file myfile.txt does not exist ?

f = open("myfile.txt", "at")
for i in range(1,11):
    f.write('Line #' + str(i) + '\n')
f.seek(0)
print(f.readline(10))
f.close()


# The file myfile.txt  is being opened using the 'at' parameter, which means "append" ('a') and "text" ('t').

# In the append mode, the file associated with the stream doesn't need to exist; if it doesn't exist, 
# it will be created; if it exists the previous content of the file remains untouched and any data 
# written to the file will be inserted at the end, after the existing data. Also, in this mode, the file cannot be read - it is only open for writing.

# So, line of code print(f.readline(10)) will raise an unhandled exception because the file cannot be read in the 'a' (append) mode.

# So, the correct answer is : The code will raise an unhandled exception.

# If the file had been opened in the Append and Read mode ('a+'), then the code would have been executed 
# correctly and the first 10 bytes of the first line of the file myfile.txt  would have been printed 
# out (as a reminder the readline() method returns one line from the file; the optional parameter 
#      specifies the number of bytes from the line to return (default -1, which means the whole line)).