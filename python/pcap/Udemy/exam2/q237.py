#!/usr/bin/python3
# What is the expected output of the following snippet ?
x=0
y=3
 
try:
    print(x%y)
    assert bool(y) == False
    print(y/x)
except ZeroDivisionError:
    print('Error 1')
except AssertionError:
    print('Error 2')
except BaseException:
    print('Error 3')
finally:
    print('Done')

# Explanation:
# This is a try-except-finally block with multiple except branches for different type of exceptions.
# In a try-except-finally block :
# --> The finally: branch is always executed.
# --> The except: branch is executed if an exception has been raised in the try: block. 
# If there are multiple except: branches, then the first one matching the exception class will be executed.
# Let's look at the code in the try: branch:
# --> print(x%y) % is the modulo operator which provides the remainder of a division - in this case 0 % 3 returns 0. No exception raised for this.
# --> assert bool(y) == False   The assert statement evaluates a condition : if the condition 
# is False, then an AssertionError  is raised; if the condition is True, then the execution of the code continue. 
# In this case bool(3) returns True , so an AssertionError  is raised.
# --> print(y/x) . This line of code is never reached because of the AssertionError  exception 
# being raised in the previous line.
# In the except: branches, the first matching the AssertionError  exception is except AssertionError:, 
# so print('Error 2') is executed. Note that BaseException is the most general exception (this is the base class)  : 
# It is placed as the last except: branch because more specific exceptions precede it.
# So, final output is :
# 0
# Error 2
# Done