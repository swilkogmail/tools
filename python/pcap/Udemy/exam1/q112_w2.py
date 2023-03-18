#!/usr/bin/python3
# What is the expected output of the following code, assuming that the file named STRWR.txt does not exist?

import errno
 
try:
    data = open("STRWR.txt", "rt")
    data.close()
except IOError as e:
    if e.errno == errno.ENOENT: # errno.ENOENT : No such file or directory
        print("A")
    elif e.errno == errno.EEXIST: # errno.EEXIST : file already exists
        print("B")
    elif e.errno == errno.EACCES: # errno.EACCES : permission denied
        print("C")
    else:
        print("D")

# Explanation:

# The IOError object is equipped with a property named errno.
# The value of the errno property can be compared with one of the predefined symbolic constants defined in the errno module.
# The most common ones are:
# In the above question, since the file that is being open does not exist, then the errno attribute of the 
# exception e will be equal to errno.ENOENT (no such file or directory) and consequently, A will be printed.