#!/usr/bin/python3
Explanation:

# Let's review each suggested answer:

# --> Each key must be unique.

# This is correct : each key in a dictionary must be unique.


# --> A key may be an integer, a string or a list.

# That is incorrect : a key must be an immutable type of object; a list is mutable.


# --> The key() method applied to a dictionary returns an iterable object consisting of all the keys within a dictionary.

# That is incorrect : the method does exist but it is named keys(), not key().



# --> The items() method applied to a dictionary returns lists where each list has two elements : a key and its corresponding value.

# That is incorrect : the items() method does exist but it returns tuples, not lists.

# each key in a dictionary must be unique:
my_dict = {'2': 1, '2': 0}
print(my_dict)    # {'2': 0}
 
# a key must be an immutable type of object:
my_dict = {'2': 1, 5: 0, (1,2): 't'}
print(my_dict)    # {'2': 1, 5: 0, (1, 2): 't'}
 
# attempting to create a dictionary with a list as a key will raise an exception:
my_dict = {[1,2]: 2}  # TypeError: unhashable type: 'list'
print(my_dict)
 
# Using the keys method:
my_dict = {'2': 1, '3': 0, '4': 5}
for key in my_dict.keys():
    print(key, end='')    # 234
 
# Using the items method:
my_dict = {'2': 1, '3': 0, '4': 5}
for x in my_dict.items():
    print(x, end=' ')    # ('2', 1) ('3', 0) ('4', 5) 