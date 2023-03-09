#!/usr/bin/python3
# Consider the following code:

dictionary = {"Luke": "Skywalker", "Han": "Solo", "Darth": "Vader"}
 
zzz
    print(x,end=',')  

# Explanation:

# This is all about methods for dictionaries.

# In the above example, "Luke", "Han" and "Darth" are keys of the dictionary, while "Skywalker", "Solo" and "Vader" are their corresponding values.

# items() is a method that returns tuples where each tuple is a key-value pair.

# keys() is a method that returns an iterable object consisting of all the keys gathered within the dictionary.

# values() works similarly to keys(), but returns values.

# vals() is not a valid method for a dictionary.

# The only code that will return Skywalker,Solo,Vader,  (values)  is for x in dictionary.values():



Try it yourself:

dictionary = {"Luke": "Skywalker", "Han": "Solo", "Darth": "Vader"}
 
for x in dictionary.items():
    print(x,end=',')            # ('Luke', 'Skywalker'),('Han', 'Solo'),('Darth', 'Vader'),
    
print('\n--------')
    
for x in dictionary.values():
    print(x,end=',')            # Skywalker,Solo,Vader,
    
print('\n--------')
 
for x in dictionary.keys():
    print(x,end=',')            # Luke,Han,Darth,
    
print('\n--------')
 
for x in dictionary.vals():     # Exception : AttributeError 
    print(x,end=',')