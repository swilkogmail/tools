#!/usr/bin/python3
# What is the expected output of the following snippet ?

def my_func(x,y):
    return x*y
 
try:
    print(my_func('C3PO',2)) # my_func('C3PO',2)  should work just fine and not raise any exception and should return C3POC3PO.
except TypeError:
    print('TypeError')
except ValueError:
    print('ValueError')
except:
    print('Error')
else:
    print('OK')
finally:
    print('Done')

# The * operator can be used with a string and an integer.

# For example :

# x='Luke'
# print(2 * x)        # LukeLuke
# So, my_func('C3PO',2)  should work just fine and not raise any exception and should return C3POC3PO.

# In a try-except-else-finally block :

# --> The else: branch  is executed when there has been no exception during the execution of the try: block.

# --> The finally: branch is always executed.

# --> The except: branch is executed if an exception has been raised in the try: block.

# So the above code should produce :

# C3POC3PO
# OK
# Done