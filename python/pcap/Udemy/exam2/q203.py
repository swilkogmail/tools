#!/usr/bin/python3
# The package is structured as follows:
# editor
#     |________videos
#     |        |______videoproc.py
#     |        |______videoedit.py
#     |
#     |________sounds
#                 |____fx
#                       |____fx1.py
#                       |____fx2.py
# You want to use the function editfx()  from the fx1  module ; you also want to rename the function editfx() as editsound() because you already have defined a function  editfx() in your program.
# Which of the code below will achieve these requirements ?

# from editor.sounds.fx.fx1 import editfx as editsound
# (Correct)

# import editor.sounds.fx.fx1
# rename editfx as editsound 

# import editor.sounds.fx.fx1.editfx as editsound

# from fx1 import editfx as editsound

# Explanation:
# When importing a module from a package that has multiple subpackages (subfolders), you need to indicate the "path" of the module in the import statement, starting from the "root" package all the way to the actual module name.
# In the case of the above package, importing any functions from the fx1 module would be done as follow:
# import editor.sounds.fx.fx1  -> this would import all the functions, methods, etc. from the fx1 module.
# To import a specific function (for example editfx()) from the fx1 module, you would use the following command :
# from editor.sounds.fx.fx1 import editfx  -> this would import the editfx() function from the fx1 module.
# To rename a function when importing it, you can use the as keyword :
# from editor.sounds.fx.fx1 import editfx as editsound   -> this is the correct answer.