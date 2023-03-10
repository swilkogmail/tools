#!/usr/bin/python3
# What is the expected output of the following code?

countries1 = ['France', 'USA', 'Italy']
countries2 = countries1 # they are the same object now
countries3 = countries1[:] # this creates a new list of all the items in coountries1
 
countries2[0] = 'England' # this added England the list that  countries1 and countries2 comprises of
countries3[1] = 'Canada' # this changes USA for Canada
 
res = 0
 
print(countries1, countries2, countries3) 
# ['England', 'USA', 'Italy'] ['England', 'USA', 'Italy'] ['France', 'Canada', 'Italy']
 
for i in (countries1, countries2, countries3):
    print(i[0])    # England -> England -> France
    if i[0] == 'England':
        res += 1
    print(i[1])    # USA -> USA -> Canada
    if i[1] == 'Canada':
        res += 2
 
print(res)         # 4


# Explanation:

# Lists are mutable objects.

# Assigning a list variable to another list variable will have those two variables 
# referencing to the same object in computer memory (they have the same identity). 
# So, when we change the values of the second list variable, the values of the first one are also changed. 
# This happens only with mutable objects.