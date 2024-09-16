#!/usr/bin/python3
"""
 This function that prints a text with 2 new lines
 after each of these characters: ., ? and :
"""


def text_indentation(text):
    """Prints text with two new lines after each of these characters: '.', '?', and ':'"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    skip_next = False
    result = []

    for idx, char in enumerate(text):
        if skip_next and char == ' ':
            skip_next = False
            continue
        elif skip_next:
            skip_next = False
        
        if char in [".", ":", "?", "!"]:
            result.append(char)
            result.append('\n')
            result.append('\n')
            skip_next = True
        else:
            result.append(char)

    print(''.join(result).strip())
