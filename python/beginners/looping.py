#!/usr/bin/python3

i = 1
while i <= 4:
    print("something")
    i += 1

# print all the letters in turn

my_input = "hello my name is steve"
for letter in my_input:
    print(letter)

# convert to a list and loop through

my_list = my_input.split()
for word in my_list:
    print(word)

my_tuple = (1, 2, 3)
for num in my_tuple:
    print(num)

my_dict = {"steve": 1, "dave": 2, "nick": 3}
# by default the iteration will only give you the keys
for name in my_dict:
    print(name)

my_dict = {"steve": 1, "dave": 2, "nick": 3}
# by default the iteration will only give you the keys
for name, num in my_dict.items():
    print(num)

# integrating conidtions

i = 1
while i <= 10:
    if i % 2 == 0:
        print(str(i) + " is an even number")
    else:
        print(str(i) + " is an odd number")
    i += 1

# continue
i = 1
while i <= 10:
    if i % 2 == 0:
        i += 1
        continue # else do nothing, it stops the execution of the loops and move on to the next one
    print(f"We're counting odd numbers {i}")
    i += 1

# continue
i = 1
while i <= 10:
    if i % 2 == 0:
        i += 1
        break # we've found one now stop searching
    print(f"We're found an odd number: {i}")
    i += 1


# else in while
i = 1
while i <= 10:
    print(i)
    i += 1
else:
    print("While loop completed")

# else in for
for i in [1,2,3,4,5,6,7,8,9,10]:
    print(i)
else:
    print("For loop completed")

# if you're just seraching for one instance in the list use break and an else can
# be used to inform that the colour is not in there
# most of the times you'd not bother with the else
colours = ['red', 'green', 'pink', 'blue', 'orange']
for colour in colours:
    print(colour)
    if colour == 'blue':
        print("blue is in the list")
        break
else:
    print("blue is not in the list")

# for loop to iterate
my_range = range(10) # up to the stop value but not including it
print(list(my_range))
# ranges use the least amount of space as it's only calulated as it's needed
my_range = range(1,14,2) # start value, stop values and step
print(list(my_range))

count = 1
while count <= 4:
        print("looping")
        count += 1

# the _ is concention to say the variable is not needed 
for _ in range(4):
    print("looping")