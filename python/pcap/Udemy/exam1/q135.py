#!/usr/bin/python3
# What is the expected output of the following code ?

def myfunc(x):
    try:
        y = 1 / x # operation 1/x where x is a string will raise an exception of type TypeError (different from ZeroDivisionError).
    except ZeroDivisionError:
        print("Failure")
    except:
        print("Error") # So, the except:  branch will be executed and print out Error
    else:
        print("Everything OK")
        return y
    finally:
        print("Completed") # Finally the finally: branch will be executed and print out Completed.


# And since the myfunc()  function does not return anything by default, None is printed out when calling :
 
print(myfunc('0'))

# Explanation:

# In the try-except-else-finally block:

# - the code within the try: part is executed when no exception has been raised

# - if an exception is raised, the code within the except: branch is executed - 
# if there are multiples  except: branches, only one branch is executed depending on the type of the exception

# - the else:  branch is executed if no exception was raised inside the try: branch.

# - the finally:  branch is always executed no matter whether an exception was raised or not

# In the above question, the myfunc()  function is called with argument '0' which is a string.

# so, operation 1/x where x is a string will raise an exception of type TypeError (different from ZeroDivisionError).

# So, the except:  branch will be executed and print out Error

# Finally the finally: branch will be executed and print out Completed.

# And since the myfunc()  function does not return anything by default, None is printed out when calling :

# print(myfunc('0'))
# All in all, the overall result is :

# Error
# Completed
# None
