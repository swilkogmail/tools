#!/usr/bin/python3
# You want to use a function named hyppo() that resides in a module named animals , 
# and it has been imported using the following line:

# import animals as hyppos

# Which statement would you use to correctly invoke the hyppo() function in your code : 


# Here the animals module is imported using aliasing. Aliasing causes the module to be 
# identified under a different name than the original - in this case the alias is hyppos.

# Because the whole module is imported, calling any entity from that module must be made 
# using both the module name and the entity name as module.entity where module is the name of the module OR its alias.

# So calling the hyppo() function is done as hyppos.hyppo().

# hyppo() would have been a correct answer if the module had been imported as : from animals import hyppo.

# animals.hyppo() wouldd have been a correct answer if the module had been imported without an alias : import animals