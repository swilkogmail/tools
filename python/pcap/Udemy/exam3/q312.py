#!/usr/bin/python3
# You have stored multiple Python modules in folder : C:\Users\luke\Documents\My_modules (on a Windows Operating System). 
# You want those modules to be available for import in a Python script you are creating.

# Which code snippet below will achieve this ?


# Explanation:

# When importing a module, Python will search for those modules in all folders defined in the path variable. That variable can be read or modified using the sys module.

# In addition, because \ is a special character, an escape character (\) must be use to represent it in a string - in other words : \\

# So, the only valid answer is :

# from sys import path
# path.append('C:\\Users\\luke\\Documents\\My_modules')