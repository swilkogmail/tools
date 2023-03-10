#!/usr/bin/python3
# Consider the following code :

name='Han'                     
                                
def jedi(nm):
    name='Luke'
    if nm==name:
        return True
    else:
        return False
 
print(jedi(name))

# Explanation:

# A variable that exists outside a function has a scope inside the function body 
# unless the function defines a variable of the same name.

# You can use the global keyword followed by a variable name to make the variable's 
# scope global (i.e. the variable will have a scope inside and outside the function).

# In the question above, the variable name='Han'  has no scope inside the function 
# since the function defines a variable with the same name (name='Luke' ).

# So, in the last line of the code, the call to function jedi() is done with parameter name='Han' which returns False.