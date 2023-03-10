#!/usr/bin/python3
# What code would you insert instead of the comment to obtain the expected output ?

# Expected output :

# Luke
# Han
# Leia

Code :

my_dict = {}
my_list = ['Luke', 'Han', 'Leia', 'Ben']
 
for i in range(len(my_list)-1): # range(3) i will be 0,1,2
    my_dict[i] = (my_list[i], ) # {0: ('Luke',), 1: ('Han',), 2: ('Leia',)}
                                # my_dict is a dictionary with keys being integer 0, 1, 2 and corresponding values are tuples : ('Luke',) , ('Han',), ('Leia',).
 
for i in sorted(my_dict.keys()):
    j = my_dict[i]   # The second for  loop will assign variable j with the values of the dictionary, which are tuples. So j is a tuple too.
    print(j[0]) # Insert your code here


# Explanation:

# The code mixes lists, tuples and dictionaries.

# The first for loop will update the initially empty dictionary my_dict as follow:

# {0: ('Luke',), 1: ('Han',), 2: ('Leia',)}
# my_dict is a dictionary with keys being integer 0, 1, 2 and corresponding values are tuples : ('Luke',) , ('Han',), ('Leia',).

# The second for  loop will assign variable j with the values of the dictionary, which are tuples. So j is a tuple too.

# To print the expected output, you need to access the first item from the tuple , - i.e. j[0]