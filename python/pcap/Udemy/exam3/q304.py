#!/usr/bin/python3
# You have the following list :

mylist = ['R2D2', 'C3PO', 'Luke', 'Han']

# Which statement would you use to get the following printed to the monitor ?
# R2D2-C3PO-Luke-Han

# Explanation:
# The join() method is a string method and returns a string in which the 
# elements of the sequence have been joined by a string str separator. The syntax is :  str.join(iterable)
# For example:
# ".".join(['L','U','K','E'])  returns   L.U.K.E
# Only  print('-'.join(mylist)) generates the expected result  : R2D2-C3PO-Luke-Han
# print(mylist, sep='-')  will only return the whole list as-is.