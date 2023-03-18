#!/usr/bin/python3
# What is the expected output of the following snippet ?
mylist1 = [[i for i in 'Luke'] for j in range(3)]

# [['L', 'u', 'k', 'e'], ['L', 'u', 'k', 'e'], ['L', 'u', 'k', 'e']] --> this is a list with 3 elements - each element is itself a list (of characters).

mylist2 =[]
for x in mylist1: # for x in mylist1: will iterate through each element of the list mylist1 (['L', 'u', 'k', 'e'] is the first element).
    for y in x: # for y in x:    will iterate through each element of ['L', 'u', 'k', 'e']   (i.e. 'L', then 'u', etc..)
        if y in mylist2:
            continue
        else:
            mylist2.append(y) # The append() method appends an element to the end of the list.
                              # So, at the end of the for loop, the list mylist2 has been 
                              # "filled" so that mylist2 is ['L', 'u', 'k', 'e'] .
        # The last else code block is executed which makes mylist2 as  ['L', 'u', 'k', 'e','!'] .
else:       
    mylist2.append('!')
print(''.join(mylist2)) # Finally the join()  method takes all items in the list and joins them into one string with the specified separator.

# Explanation:

# [[i for i in 'Luke'] for j in range(3)]   will return a list of lists :

# [['L', 'u', 'k', 'e'], ['L', 'u', 'k', 'e'], ['L', 'u', 'k', 'e']] --> this is a list with 3 elements - each element is itself a list (of characters).

# for x in mylist1: will iterate through each element of the list mylist1 (['L', 'u', 'k', 'e'] is the first element).

# for y in x:    will iterate through each element of ['L', 'u', 'k', 'e']   (i.e. 'L', then 'u', etc..)

# The append() method appends an element to the end of the list.

# So, at the end of the for loop, the list mylist2 has been "filled" so that mylist2 is ['L', 'u', 'k', 'e'] .

# The last else code block is executed which makes mylist2 as  ['L', 'u', 'k', 'e','!'] .

# Finally the join()  method takes all items in the list and joins them into one string with the specified separator.

# In this case, ''.join(mylist2) returns Luke! .