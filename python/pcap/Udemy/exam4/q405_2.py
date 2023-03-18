#!/usr/bin/python3
# You want to check which version of Python your development environment is using.
# Which code snippet below would provide this information ?

# import platform
# print(platform.python_implementation())

# import platform
# print(platform.platform())

# import platform
# print(platform.version())
# (Incorrect)

# import platform
# print(platform.python_version_tuple())
# (Correct)

# Explanation:
# The platform module contains functions which provides information on the Python environment, the underlaying Operating System and the hardware.
# The platform()  function returns a string describing the environment (OS + processor).
# The version()  function returns the OS version as a string.
# The python_implementation() function returns the Python implementation as a string (most common is "CPython").
# The python_version_tuple()  returns a three-element tuple filled with the Python version (major part, minor part, patch level number).
# So, the correct answer is :
# import platform
# print(platform.python_version_tuple())

import platform
 
print(platform.python_version_tuple())
# ('3', '8', '5')
 
print(platform.version())
# 10.0.19041
 
print(platform.python_implementation())
# CPython
 
print(platform.platform())
# Windows-10-10.0.19041-SP0