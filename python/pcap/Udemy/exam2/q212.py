#!/usr/bin/python3
# What is the output of the following snippet ?
my_list = {'a': ord('a'), 'b': ord('b'), 'c': ord('c'), 'd': ord('d') } # my_list is a dictionary (the poorly chosen name was selected to confuse you).
# The ord() function returns the Unicode code from a given character. So my_list is a dictionary that looks like this :
# {'a': 97, 'b': 98, 'c': 99, 'd': 100}
list=[]
list2=[]
for i in sorted(my_list.keys()):
    # The for loop simply insert each value from the dictionary in the list list using the insert() method.
    print(i)
    print(my_list[i])
    list.insert(-1,my_list[i]) # -1 put the next value into the penultimate value in the list
    list2.insert(0,my_list[i]) # 0 will put the next value into the front of the list
    print(list)
    print(list2)
 




# The  insert() method inserts a given element at a given index in a list. The syntax is :
# list_name.insert(index, element).
# In this case, index = -1 ;pay particular attention to the behavior of the insert() method in this case - see print out below for details.