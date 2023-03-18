#!/usr/bin/python3
# What is the expected output of the following code ?

class Delta:
    D=1
    def __init__(self, d):
        self.__d = d + 1
        # Property d is defined as a private instance variable (note the double underscores). Such a property is still 
        # accessible from outside the class using a mangled name constructed as _ClassName__PrivatePropertyName.
try:
    d = Delta(1)
    print(d.__d)
    # So, in the above code, line print(d.__d) will raise an exception (AttributeError) since it's 
    # not using the mangled name to access the private instance variable d. Since this line is inside a
    # try:except: branch, the exception will be caught and the code inside the except: branch will be executed and Error will be printed.
except:
    print("Error")
else:
    print("All good")
    # The code inside the else: branch will not be executed (it would have been executed if no exception had been raised).
finally:
    print("Done")

# Explanation:


# And the code inside the finally:  branch is always executed whether or not an exception is raised : so Done will be printed.

# Conclusion, the correct answer is :

# Error
# Done