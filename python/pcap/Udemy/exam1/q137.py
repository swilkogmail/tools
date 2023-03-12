#!/usr/bin/python3
# Which statement is true about the following line of code (Pick two) ?

# f = open('myfile.txt','r+t')
# Explanation:

# The open() function allows to associate a file with a stream which can then be processed. 
# The first parameter is the name of the file, and the second parameter is the open mode.

# r+ is the open mode : read and update. In this case :

# 1/ the stream will be opened in read and update mode;

# 2/ the file associated with the stream must exist and has to be writeable, otherwise the open() function raises an exception;

# 3/ both read and write operations are allowed for the stream.

# The t at the  end of the open mode string means that the stream will be opened in text mode (as opposed to binary mode which would be a b).
# 