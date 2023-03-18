#!/usr/bin/python3
try:
    raise Exception(a,b,c)
except Exception as e:
    print(len(e.args))