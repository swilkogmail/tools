#!/usr/bin/python3
def split_names(names):
    return names.split(',')

def is_palindrome(name):
    pal = False
    rev_name = (name[::-1])
    # print(rev_name)
    if rev_name == name:
        pal = True
    return pal

def build_list(item, count):
    return_list = []
    for _ in range(count):
        return_list.append(item)
    return return_list

my_list = build_list("hello", 10)
print(my_list)

name_list = split_names('steve,seb,chantelle,radar')
print(name_list)

for name in name_list:
    is_pal = is_palindrome(name)
    if is_pal:
        print(name, "is a palindrome")
    else:
        print(name, "is not a palindrome")
        
