#!/usr/bin/env
def uppercase(str):
    for i in range (len(str)):
        s = str[i]
        uppercase = ord(s)
        if uppercase >= 97 and unicode <= 122:
            s = chr(uppercase - 32)
        print("{:s}".format(s), end="")
    print("")
