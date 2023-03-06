#!/usr/bin/python3
from collections import deque
# items = deque([1, 2])
# items.append(3)        # deque == [1, 2, 3]
# items.rotate(1)        # The deque is now: [3, 1, 2]
# items.rotate(-1)       # Returns deque to original state: [1, 2, 3]
# item = items.popleft() # deque == [2, 3]
# print(deque.__doc__)

# rotate=
# print(sharp_notes)

# 1. handle enharmonic notes, i.e. work out whether to convert
# C#,D#,F,F#,G#,A#,C to C#,D#,E#,F#,G#,A#,B# for C# Major
# 2. exceptions

# key = input("enter a key to get the notes for major scale: ")

def major_scale(key):
    all_notes = ["A", "A#", "B", "C", "C#", "D", "D#","E", "F", "F#","G", "G#"]
    intervals = ["1", "m2", "M2","m3","M3", "P4","b5","P5","m6","M6","b7","M7"]
    i  = all_notes.index(key)
    nt_q = deque(all_notes)
    nt_q.rotate(-i)
    chromatic_scale = [*nt_q]
    major_scale_d = dict(zip(intervals, chromatic_scale))
    return f"{key} Major Scale is {major_scale_d.get('1')},{major_scale_d.get('M2')},{major_scale_d.get('M3')},{major_scale_d.get('P4')},{major_scale_d.get('P5')},{major_scale_d.get('M6')},{major_scale_d.get('M7')}"

def major_scale2(key):
    all_notes = [
                "A", "A#", "B",
                ["B#", "C"], "C#", "D",
                "D#", "E", ["E#", "F"],
                "F#", "G", "G#"
                ]
    intervals = ["1", "m2", "M2", 
                "m3", "M3", "P4", 
                "b5", "P5", "m6",
                "M6", "b7", "M7"
                ]
    if key == "C":
        i = 3
    elif key == "C#":
        i = 4
        print(all_notes[3])
        all_notes[3].pop(1)
        all_notes[8].pop(1)
    else:
        i  = all_notes.index(key)
    # print(f"location of {key} in list is {i}")
    nt_q = deque(all_notes)
    nt_q.rotate(-i)
    chromatic_scale = [*nt_q]
    d = dict(zip(intervals, chromatic_scale))
    print(f"this is the scale that needs some work {d}")
    major_scale_list = d.get('1'),d.get('M2'),d.get('M3'),d.get('P4'),d.get('P5'),d.get('M6'),d.get('M7')
    for note in major_scale_list:
        print (f"note is {note}")
    print(major_scale_list)
    print(f"{key} Major Scale is {d.get('1')},{d.get('M2')},{d.get('M3')},{d.get('P4')},{d.get('P5')},{d.get('M6')},{d.get('M7')}")


# my_scale = major_scale2("C")
my_scale = major_scale2("G")
# my_scale = major_scale2("D")
# my_scale = major_scale2("A")
# my_scale = major_scale2("E")
# my_scale = major_scale2("B")
# my_scale = major_scale2("F#")

# all_notes = [
#             "A", "A#", "B",
#             ["B#", "C"], "C#", "D",
#             "D#", "E", ["E#", "F"],
#             "F#", "G", "G#"
#             ]
# intervals = ["1", "m2", "M2", 
#              "m3", "M3", "P4", 
#              "b5", "P5", "m6",
#              "M6", "b7", "M7"
#             ]

# print(all_notes)
# print(all_notes[3][1])
# print(intervals)
# d = dict(zip(intervals, all_notes))
# print(d.get("m3"))
# m3_v1 = (d.get("m3"))[0]
# m3_v2 = (d.get("m3"))[1]
# m6_v1 = (d.get("m6"))[0]
# m6_v2 = (d.get("m6"))[1]
# print(f"minor 3 has two enhamonically equiv notes: {m3_v1} & {m3_v2}")
# print(f"minor 6 has two enhamonically equiv notes: {m6_v1} & {m6_v2}")