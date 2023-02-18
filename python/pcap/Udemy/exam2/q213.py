#!/usr/bin/python3
# What is the expected output of the following snippet ?

l={} # The l variable is an empty dictionary initially.
for i in 'Skywalker':
    if i in 'Vader':
       l[ord(i)]=i
else: # In a for-else loop, the else: clause is executed when the code below the for loop has completed successfully - 
      # in this case the code in the else: clause adds the following key:value pair to the dictionary : 100:'d'.
    l[ord('d')]='d' 
 
for j in l.keys():
    print(l[j], end=' ')

# numbered list containing 3 elements
# ord d will be returned multiple times although deduplicated as its a dictionary
# printing keys not values so we should have a e r and d


# The for loop populates the dictionary with the characters from the string 'Skywalker" that are in the string 'Vader' (i.e. a, e and r) : 
# those are the values of the dictionary while the corresponding keys are the Unicode code of the corresponding character (the ord() 
# function returns the Unicode code of a character).

# So by the end of the first for-else loop, the l dictionary is as follow:
# {97: 'a', 101: 'e', 114: 'r', 100: 'd'}
# The last for loop, simply print each value from the l dictionary using the end parameter of the print() function to have the characters nicely printed on one line, separated by a space.
# Resulting output is :
# a e r d


