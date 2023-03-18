#!/usr/bin/python3
# What is a possible output from the code snippet below :
from platform import machine
print(machine())

from platform import platform, machine, processor, system, version, python_implementation
 
print(platform())
# Windows-10-10.0.19041-SP0
 
print(machine())
# AMD64
 
print(processor())
# Intel64 Family 6 Model 78 Stepping 3, GenuineIntel
 
print(system())
# Windows
 
print(version())
# 10.0.19041
 
print(python_implementation())
# CPython