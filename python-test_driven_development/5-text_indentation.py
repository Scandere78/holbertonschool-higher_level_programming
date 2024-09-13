#!/usr/bin/python3
"""
 This function that prints a text with 2 new lines
 after each of these characters: ., ? and :
"""


def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = []
    skip_next = False

    for i in text:
        if skip_next:
            if i == ' ':
                continue
            skip_next = False

        if i in [".", ":", "?", "!"]:
            result.append(i)
            result.append('\n')
            result.append('\n')
            skip_next = True
        else:
            result.append(i)

    print(''.join(result).strip())
