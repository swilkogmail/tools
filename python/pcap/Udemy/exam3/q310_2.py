#!/usr/bin/python3
# Consider the code below:
x = 'Tatooine is a lawless place ruled by Hutt gangsters.'
# Insert line of code here.

# Which snippet would you insert in order for the program to output the following result:
# Tatooine Is A Lawless Place Ruled By Hutt Gangsters. 


# Explanation:
# Let's review each suggested answers :
# --> print(x.capitalize()) : capitalize() will return the same string but with the first character 
#     converted to upper-case and the remaining characters converted to lower-case. This will not produce the expected result.
# --> print(x.upper()) : upper() will return the same string but with all characters 
#     converted to upper-case. This will not produce the expected result.
# --> print(x.swapcase()) : swapcase() will return the same string 
#     but each character has its case swapped. This will not produce the expected result.
# --> print(x.title()) : title() will return the same string but with the 
#     first character of each word converted to upper-case : this will produce the expected result.
# Try it yourself:
# x = 'Tatooine is a lawless place ruled by Hutt gangsters.'
 
print(x.capitalize()) # Tatooine is a lawless place ruled by hutt gangsters.
 
print(x.upper()) # TATOOINE IS A LAWLESS PLACE RULED BY HUTT GANGSTERS.
 
print(x.swapcase()) # tATOOINE IS A LAWLESS PLACE RULED BY hUTT GANGSTERS.
 
print(x.title()) # Tatooine Is A Lawless Place Ruled By Hutt Gangsters.