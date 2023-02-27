#!/usr/bin/python3
# What is the expected output of the following code snippet ?

my_list = ['carrot', 'potato', 'cauliflower', 'radish']
my_list.sort(key = lambda x: x[-2], reverse= True)
print(my_list)

# Explanation:

# sort() is a method of the list class. It is similar to sorted() but with a few differences :

# - sorted() returns a new sorted list, while sort() sorts the list in place

# - sorted() can be used with an iterable (like a string for example), while sort() can only be used with lists.

# Both sort() and sorted() can be used with one of these optional keyword arguments:

# - reverse : if set to True, sorting is done in a descending order - if set to False, sorting is done in ascending order.

# - key : this argument is a function which will be used on each value in the list being sorted to determine the resulting order.

# In the above question, they key argument is used in the sort() method, with key = lambda x: x[-2]  
# -> this is a lambda function that will be applied on each element of my_list  - this lambda function 
# will extract the second to last character for each of the strings in my_list . For example : the lambda 
# function applied to 'carrot' will return 'o' . The sort() method will then perform the sorting operation 
# based on those resulting characters (note that the original strings are still returned; they are not 
# actually modified by the function identified by key - the function in key is only used to figure out what to sort).

# So, based on their second to last character, sorting the elements of my_list in ascending order will return :

# ['cauliflower', 'carrot', 'radish', 'potato']

# However, keyword argument reverse has been set to True, so the order is returned in a descending fashion :

# ['potato', 'radish', 'carrot', 'cauliflower']