#!/usr/bin/python3
# What is the expected output of the following code, assuming that the file named myfile.txt exists and has read only attribute ?

import errno
 
try:
    data = open("myfile.txt", "w")
    data.close()
    print("Done")
except IOError as e:
    if e.errno == errno.ENOENT:
        print("A")
    elif e.errno == errno.EMFILE:
        print("B")
    elif e.errno == errno.EACCES:
        print("C")
    else:
        print("D")

# Explanation:

# The IOError object is equipped with a property named errno.

# The value of the errno property can be compared with one of the predefined symbolic 
# constants defined in the errno module.

# The most common ones are:

# errno.ENOENT : No such file or directory

# errno.EACCES : permission denied

# errno.EMFILE: Too many open files

# In the above question, since the file that is being open for writing has a read-only attribute, 
# then the errno attribute of the exception e will be equal to errno.EACCES (permission denied) and, consequently, C will be printed.