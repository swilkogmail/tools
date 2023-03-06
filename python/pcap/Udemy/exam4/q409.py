#!/usr/bin/python3
# Which statement below, related to Python exceptions, is true ?

# Explanation:

# Let's review each suggested answers:

# --> The Exception class is the most general of all Python exceptions.

# That's incorrect : the most general of all Python exceptions is the BaseException.



# --> The KeyError exception class is more concrete than the LookupError  exception class.

# This is true ! The KeyError exception is a sub-class of the LookupError  exception class and, as such, 
# is considered more concrete (or less general/abstract) than LookupError . The actual relationship is as below:

# BaseException ← Exception ← LookupError ← KeyError



# --> The ValueError exception class is a sub-class of the ArithmeticError class.

# That is incorrect. ValueError is a sub-class of the Exception class.



# --> ImportModuleError  is an exception raised when an import operation fails.

# That is not correct : the exception that is raised when an import fails is the ImportError exception, which is located as shown here :

# BaseException ← Exception ← StandardError ← ImportError