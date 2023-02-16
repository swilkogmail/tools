#!/usr/bin/python3
# in order to keep __upper private the interpreter will mangle the name
# to produce a unique name so it can't be referenced outside the class as update

class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)
                      
    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update

class MappingSubclass(Mapping):
    def update(self, keys, values):
        for item in zip(keys, values):
            self.items_list.append(item)
    
    def print_something(self):
        print("Print Something")

    __update = print_something

# print (Mapping.__update) # this will result in an error as there is no name __update
print(dir(Mapping)) # this will return a '_Mapping__update' name which is unqiue to its class
print(dir(MappingSubclass))  # this will return _MappingSubclass__update as well as _Mapping__update as we have access to both


