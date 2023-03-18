#!/usr/bin/python3
# Consider the snippet below :

my_list = ['R2D2', 'C3PO']
print(' is friend with '.join(my_list))
print(','.join(my_list)) 


# Which code snippet would you replace zzz with to get the following printed to the monitor ?

# R2D2 is friend with C3PO

# string.join(iterable)  where:

# string : this is the string separator that will be used to join the elements of the iterable into one string.

# So, in the above question : print(' is friend with '.join(my_list))  will return :
# R2D2 is friend with C3PO   (string ' is friend with '  is used as the separator between element 'R2D2' and 'C3PO')

# Let's review the other suggested answers:

# print(my_list[1] + ' is friend with ' + my_list[2])  -> my_list[2]  is the 
# 3rd element in the list my_list (index always starts at 0) and my_list  has only two elements - so this will raise an exception.

# print(my_list.join(' is friend with '))  -> that's not the correct usage of the join() method : join()  
# will expect a string as a separator, not a list : this will raise an exception.

# my_list.insert(1,' is friend with ')  -> this will insert the string ' is friend with '  
# at index 1 in the list my_list  and   print(my_list) will print the whole list : ['R2D2', ' is friend with ', 'C3PO']  which is not the expected result.