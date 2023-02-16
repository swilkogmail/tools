#!/usr/bin/python3
from scale import Scale
from mode import Mode

CMajor=Scale('C', 'Major', 'major')
print(CMajor)
print(CMajor.key)
print(CMajor.name)
print(CMajor.type)
# print(CMajor.description)
print(CMajor.description())
# print(dir(Scale))
####
AAeolian=Mode('A', 'Aeolian', 'minor', ['A','B','C','D','E','F','G']) 
print(AAeolian.key)
print(AAeolian.name)
print(AAeolian.type)
print(AAeolian.notes)
print(AAeolian.description())
print(dir(Mode))
# inspecting our __str__ representations
print(str(AAeolian))
print(str(CMajor))