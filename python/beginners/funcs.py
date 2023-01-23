#!/usr/bin/python3
# start with a lower case (or _ indicates it's a hidden function)
def print_something(something):
    pass

def print_name(name):
    print(f"Name is {name}")

print_name('steve')

output = print_name('steve')

# this will not return anything as the function writes to the screen doesn't return anything
print(output)

# to fix this use a return statement

def print_name(name):
    return "Name is "+ name

output = print_name('steve')

print(output)

## parameters vs arguments
# name, age and car_model are parameters
def contact_card(name, age, car_model):
    return f"{name} is {age} and drives a {car_model}"

# when called steve, 48 and merc are arguments
details = contact_card('steve', 48, 'merc')

print(details)

# key words and argumemts
details = contact_card(age=48, car_model='honda', name='barry',)

print(details)

# key words, positional and argumemts
details = contact_card('percy', age=48, car_model='honda')

print(details)

# key words, positional and argumemts Error as started with a key words
# details = contact_card(name='percy', 48, car_model='honda')

# print(details)

# setting a default
def can_drive(age, driving_age=18):
    return age >= driving_age

# returns true
can_drive(29)

# override a default
def can_drive(age, driving_age=18):
    return age >= driving_age

# returns false
can_drive(29,30)

# once you start to define default values then teh remaining parameters also have to be
# defined with default values

# recursion - calling function from inside itself
