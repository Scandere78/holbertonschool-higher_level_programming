#!/usr/bin/python3
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    skip_next = False
    for idx, i in enumerate(text):
        if skip_next:
            skip_next =  False
            continue
        if i in [".", ":", "?", "!"]:
            print(i, end="\n")
            print()
            skip_next = True
        else:
            print(i, end="")