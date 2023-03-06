#!/usr/bin/python3
# You are being asked to create a Python program that will randomly return five unique 
# integers between 0 and 100 (both 0 and 100 are included as possible choices).

# Which code will achieve this requirement ?

# Explanation:

# Let's review each suggested answers:

# --> print("Selected numbers are: ", random.randrange(0,101,5))

# Function randrange(start, stop[, step])  (or randrange(stop)) returns one randomly selected 
# element from range(start, stop, step).  So, random.randrange(0,101,5)) will return one 
# integer from range(0,101,5) . The requirement calls for five integers, not one - so this will not work.

# --> print("Selected numbers are: ", [random.randint(0,101) for x in range(5)])

# Function randint(a, b) returns a random integer N such that a <= N <= b.  So, [random.randint(0,101) 
# for x in range(5)]  (a list comprehension) will return a list of five integers between 0 and 101 (included) - 
# also those elements will not necessarily be unique. So this is not complying with the requirements and it is not the correct answer.

# --> print("Selected numbers are: ", random.choices(range(101),k=5))

# Function choices(population, k=1) returns a k sized list of elements chosen from the population - 
# those elements may be repeated. So, random.choices(range(101),k=5)  will return a list of five non-unique 
# integers between 0 and 100 (included). Because the requirement calls for uniqueness, this answer is incorrect. 
# Note : the choices() function has some additional optional weight parameters not discussed here.

# --> print("Selected numbers are: ", random.sample(range(101),k=5))

# Function sample(population, k) returns a k length list of unique elements chosen from the population 
# sequence. So, random.sample(range(101),k=5)  will return a list of five unique integers between 0 
# and 100 (included). This is exactly what the requirement calls for and this is the correct answer. 
# Note : the sample() function has one additional optional parameter not discussed here.