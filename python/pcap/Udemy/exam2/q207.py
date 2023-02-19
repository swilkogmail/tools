#!/usr/bin/python3
# What is the expected output of the following code snippet ?
my_list = ['apple', 'koala', '1234Bz', 'Polo']
my_list.sort(key = lambda x: x[::-1]) # -> this is a lambda function that will be applied on each element of my_list (each character in each element in the list)
print(my_list)
print(my_list[0])

# Explanation:
# sort() is a method of the list class. It is similar to sorted() but with a few differences :
# - sorted() returns a new sorted list, while sort() sorts the list in place
# - sorted() can be used with an iterable (like a string for example), while sort() can only be used with lists.
# Both sort() and sorted() can be used with one of these optional keyword arguments:
# - reverse : if set to True, sorting is done in a descending order - if set to False, sorting is done in ascending order.
# - key : this argument is a function which will be used on each value in the list being sorted 
# to determine the resulting order.
# In the above function, they key argument is used in the sort() method, with key = lambda x: x[::-1]  
# -> this is a lambda function that will be applied on each element of my_list  - this lambda function 
# will reverse the order of the characters for each of the strings in my_list . For example : 'apple' 
# will become 'elppa' ; 'koala' will become 'alaok', etc.. The sort() method will then perform the 
# sorting operation based on the first letter of these modified strings ('elppa', 'alaok', etc...) 
# but the original strings are still returned (they are not actually modified by the function identified 
# by key - the function in key is only used to figure out what to sort).
# Based on this, 'alaok' would be the first string (because it starts with character 'a' which has the 
# smallest Unicode value among lowercase letters). The second one will be 'elppa'. Third one is 'oloP' and last one is 'zB4321'.
# And so, my_list.sort(key = lambda x: x[::-1])  will return :
# ['koala', 'apple', 'Polo', '1234Bz']  (remember that the list is not modified by the function in key, it is just used for ordering).