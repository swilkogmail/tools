#!/usr/bin/python3
# What is the expected output of the following code, assuming that the file named myfile.txt does exist?

import errno
 
try:
    data = open("myfile.txt", "x")
    data.write("123")
    data.close()
except IOError as e:
    if e.errno == errno.ENOENT:
        print("A")
    elif e.errno == errno.EEXIST:
        print("B")
    else:
        print("C")
else:
    print("D")

# Explanation:
# The IOError exception object is equipped with a property named errno.
# The value of the errno property can be compared with one of the predefined symbolic constants defined in the errno module.
# The most common ones are:
# errno.ENOENT : No such file or directory
# errno.EACCES : permission denied
# errno.EEXIST : file already exists

# In the above question, myfile.txt is being opened with the x mode. With the x mode, the file 
# will be opened for exclusive creation : The file must not exist before open  and  the 
# file will be created after open. If if the file already exists when opening it with the x mode, 
# then an exception FileExistsError will be raised. This exception is equivalent to an IOError  exception with errno value equal to errno.EEXIST .
# Because myfile.txt already exists when line of code data = open("myfile.txt", "x") is 
# executed, this will raise an exception and the errno attribute from the IOError exception 
# object  e will be equal to errno.EEXIST (file already exists) and consequently, B will be printed.