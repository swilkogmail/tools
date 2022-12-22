#!/usr/bin/python3
# single quotes and double quotes are the same although
# can be changed if you need to use a ' or a " inside the string
print('pass')
print("word")
print('''This
is a 
multi line string''')

var ='''This
is a 
multi line string'''
print(var)
# var will be stored as a single lines with /n characters

var = 'ha'
var *= 4 # multiple var by 4 times and reassign to var
print(var)

'''
Objects encapsulate two things
    state: 
        in string it's sequence of characters, it's what the object holds
    behaviour:
        method these can act on the state
'''
var = 'my_string' # my_string is the state
print(var.upper()) # upper is the method

# escape sequences
print("Tab\tDelimited")
print("New\nLine")
print("New\\nLine") # unescaped sequence