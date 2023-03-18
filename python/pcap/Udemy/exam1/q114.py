#!/usr/bin/python3
# What is the expected output of the following snippet ?

def list_func(x):
    try:
        return x[4]/x[-1]
    except ZeroDivisionError:
        print("Function Error #1")
        raise
    except IndexError:
        print("Function Error #2")
        raise
    except:
        print("Function Error #3")
        raise
 
my_list=[3,4,1,0]
try:
    print(list_func(my_list))
except LookupError: # IndexError exception which is a subclass of LookupError exception.
    print("Program Error #1")
except ArithmeticError:
    print("Program Error #2")
except:
    print("Program Error #3")

# Explanation:

# Function list_func() returns the result of the division of the 5th element (index 4) of the argument x by the last element (index -1) of the argument x.

# list_func(my_list)  where my_list=[3,4,1,0]  will raise an exception because the list has only 4 elements.

# This type of exception is an IndexError exception which is a subclass of LookupError exception.

# So, the clause except IndexError:  in the function list_func()  will be executed and Function error #2 will be printed.

# In addition, because of the raise command, the same IndexError exception is raised again - but this time the 
# exception is handled outside of the function list_func(). The except LookupError: clause is the first one matching 
# the IndexError exception and consequently Program Error #1 is printed.

# So correct answer is :

# Function Error #2
# Program Error #1