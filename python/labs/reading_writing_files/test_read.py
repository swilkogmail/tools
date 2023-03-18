#!/usr/bin/python3

file_name = 'test.txt'

 
with open(file_name, "r") as f:
    # f.seek(file_name + 1)
    file_body = f.read()

print(file_body)