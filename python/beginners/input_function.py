#!/usr/bin/python3
# pause and return the input
#input()

numb = int(input("Choose a number: "))
colour = input("Choose a colour: ")
name = input("Choose a name: ")

print('You chose number: ' + str(numb))
print(' and ' + colour)
print(' and ' + name)

# single space is the default so sep, in this example is redundant
print('You chose', numb, 'and', colour, 'and', name + '.', sep=" ")