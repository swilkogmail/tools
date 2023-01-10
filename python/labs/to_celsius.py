#!/usr/bin/python3
fahrenheit = float(input("Enter the temp in Farenheight to convert to Celcius: "))

celsius = int(((fahrenheit - 32) * 5/9))

print(fahrenheit, "F in Celsius is", round(celsius, 2),"C")