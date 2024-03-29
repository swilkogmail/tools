#!/usr/bin/env python3
from collections import deque
import sys

def sharp_keys(key):
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
    else:
        i  = all_notes.index(key)
    nt_q = deque(all_notes)
    nt_q.rotate(-i)
    chromatic_scale = [*nt_q]
    d = dict(zip(intervals, chromatic_scale))

    major_note_opts = d.get('1'),d.get('M2'),d.get('M3'),d.get('P4'),d.get('P5'),d.get('M6'),d.get('M7')
    
    major_scale_notes = []
    # work out which of the enharmonic note options to take
    for note in major_note_opts:
        if isinstance(note,str):
            major_scale_notes.append(note)
    for note in major_note_opts:
        if isinstance(note,list):
            opt1 = note[0][0]
            # print(f"option1: {opt1}")
            if opt1 not in major_scale_notes:
                major_scale_notes.append(note[0])
            else:
                major_scale_notes.append(note[1])
    # sort (as append changes order) and resort in key order
    major_scale_notes = sorted(major_scale_notes)
    i  = major_scale_notes.index(key)
    nt_q = deque(major_scale_notes)
    nt_q.rotate(-i)
    major_scale_list = [*nt_q]
    return major_scale_list


sharp_keys_list = ['C','G','D','A','E','B','F#','C#']

print("All sharp keys...")
for key in sharp_keys_list:
    notes = sharp_keys(key)
    print(notes)

key = input("Input a key to find out all the notes in the major scale: ").upper()

try:
   notes = sharp_keys(key)
except ValueError as err:
    print(f"ERROR: '{key}' is not a valid sharp key, choose from 'C','G','D','A','E','B','F#','C#'. Message: ({err})")
    sys.exit(1)
else:
    print(notes)