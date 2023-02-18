#!/usr/bin/python3
# What is the expected output of the following code ?
list_1 = list('Chewie')
print(list_1)
list_2 = list('Han')
list_3 = list('Luke')
# list_1, list_2 and list_3 are lists.
try:
    list_1=list_2 # = 'H','a','n'
    # list_1 and list_2 points to the same list in memory. You can convince yourself
    # by checking id(list_1) against id(list_2) : they are the same (see "Try it yourself" 
    # section for details) which proves that those two variables points to the same object.
    list_2.insert(0,list_3[0]) # list_2 = ['L','H','a','n'
    assert list_1[0] == 'H' # this will check and raise an erro if false
except:
    print('Error')
else:
    print('OK') # it's not an exception so OK
finally:
    print('Done') # always raised

Error
Done

# Explanation:
# Assignment list_1=list_2  (first line in the try: block) will make variables 
# Line list_2.insert(0,list_3[0])  will insert the first element of list_3 at the index 
# 0 of list_2. In other words, this will update list_2 as : ['L', 'H', 'a', 'n'].
# Because variables list_1 and list_2 points to the same object, we also have list_1 as ['L', 'H', 'a', 'n'].
# Now, the third line in the try: block  (assert list_1[0] == 'H') will check the 
# expression list_1[0] == 'H'  and raise an exception if the expression is False - t
# his is actually the case : so the AssertError exception is raised and code in the except: block is executed.
# As a reminder, in a try-except-else-finally block :
# --> The else: branch  is executed when there has been no exception during the execution of the try: block.
# --> The finally: branch is always executed.
# --> The except: branch is executed if an exception has been raised in the try: block.