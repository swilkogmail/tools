#!/usr/bin/python3
# Question 15: Correct
# You have installed package fin that has two sub-packages fin1 and fin2 , 
# each containing two modules as below :
# --fin
#     +--fin1
#     +   +--mod1.py
#     +   +--mod2.py
#     +--fin2
#     +   +--mod3.py
#     +   +--mod4.py
# You would like to use the function func() from module mod2.py  in your 
# Python program; however, you already have defined a function func() in your 
# program and you would like to rename the func() function from the fin package as finfunc().
# Which code will allow you to correctly import what you need, based on the above requirements ?

# Explanation:
# Importing entities from a module mod located in a nested package is done using 
# the dot notation, separating the package name from the subpackage name :
# import package.subpackage.mod  This will import all entities from module mod.
# Or alternatively : from package.subpackage import mod
# To import a specific entity from module mod (for example function foo), use the following statement :
# from package.subpackage.mod  import foo
# Finally, to rename an entity (using an alias) during import, use the following statement :
# from package.subpackage.mod  import foo as foonew : this will import function foo using alias foonew.