#!/usr/bin/python3
What is the expected output of the code below?

my_l = [[i+j for i in range(1,5,1)] for j in range(-1,6,3)]
# 3 loops executed for -1,2,5
# passing -1 then 2 then 3 in to [1,2,3,4,5]
# resuliung in [[0, 1, 2, 3], [3, 4, 5, 6], [6, 7, 8, 9]]

my_p =[]
for l in my_l: #  [[0, 1, 2, 3], [3, 4, 5, 6], [6, 7, 8, 9]]
    for k in l:
        if k not in my_p: # it's orginally empty then populated with 0,1,2,3 first time, then 4,5,6 second time (as 3 is already in the list), etc..
            my_p.append(k)
 
print(my_p)

# Explanation:
# my_l is defined using the list comprehension "method"  - which results in the following list :
# [[0, 1, 2, 3], [3, 4, 5, 6], [6, 7, 8, 9]]
# The for loops go through each element of the list my_l - and because it is a list of list (matrices), two for loops are necessary.
# For each of those elements k, if they are not already in list my_p (if k not in my_p:) 
# then the element k is added in the my_p list using the append() method 
# (as a reminder mylist.append(x) will add at the end of list mylist the element x).
# The resulting output is :
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]