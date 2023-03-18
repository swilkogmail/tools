#!/usr/bin/python3
my_list = ["steve", "gary", "barry", "bob", "tracy", "ian"]
print(my_list)
# remove an item
bob_i = my_list.index("bob")
print(bob_i)
del (my_list[bob_i])
print(my_list)
# reserve the list
my_list_rev = list(reversed(my_list))
print(my_list_rev)
# slice to return 3rd and 4th
len_list = len(my_list_rev)
print("length of list: " +  str(len_list))
print(my_list[2:4])
# insert an item
new_item = ["melody"]
my_list += new_item
# my_list = my_list.insert(0, new_item)
print("new list :" + str(my_list))