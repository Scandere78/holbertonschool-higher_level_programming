#!/usr/bin/python3
"""
 This function that prints a text with 2 new lines
 after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    Return: the result of the text
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    skip_next = False
    for idx, i in enumerate(text):
        if skip_next and i == ' ':
            skip_next = False
            continue
        elif skip_next:
            skip_next = False
        if i in [".", ":", "?", "!"]:
            print(i, end="\n\n")
            skip_next = True
        else:
            print(i, end="")

 