#!/usr/bin/python3
colours = ['red', 'blue', 'green', 'yellow']
upper_colours = []
for colour in colours:
    upper_colours.append(colour.upper())

print(upper_colours)

colours = ['red', 'blue', 'green', 'yellow']
upper_colours = [colour.upper() for colour in colours]
print(upper_colours)

colours = ['red', 'blue', 'green', 'yellow']
warm_colours = [colour.upper()  for colour in colours if colour in ['red','yellow']]
print(warm_colours)