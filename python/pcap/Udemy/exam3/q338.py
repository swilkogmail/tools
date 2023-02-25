#!/usr/bin/python3
# What is the expected output of the following code, assuming the file myfile.txt does not exist ?

L = ["ABC\n" for x in range(10)]
f = open("myfile.txt", "w+")
f.writelines(L)
print(f.read())
f.close()


# The first line of the code will create a list L containing 10 elements - each element being the string "ABC\n".
# The file myfile.txt  is being open in mode "w+" which means write and update. In this mode, the 
# file associated with the stream doesn't need to exist; if it doesn't exist, it will be created; both read and write operations are allowed for the stream.
# The writelines() method writes the items of a list to a file.
# So, the first three lines of the above code will work correctly (no exception is raised) : the content of the list L will be printed to the file.
# The 4th line of the code will print the content of the file to the screen but starting at the current 
# file position (end of the file at this point) and so no visible character will be printed out.
# So, the correct answer is :The code will not raise an exception but will not print any visible characters.
# To allow the whole content of the file to be printed to the screen correctly, the file position should 
# have been reset to the beginning of the file - this can be done using the method seek() which allows 
# to move the stream reader to a particular location in the stream. In the above code adding f.seek(0) 
# prior to the line print(f.read()) would have printed all 11 lines of the file to the screen.

