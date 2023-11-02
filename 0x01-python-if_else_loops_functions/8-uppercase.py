#!/usr/bin/python3
def is_lowerletter(c):
    if (c >= 'a' and c <= 'z'):
        return (chr(ord(c) - 32))
    else:
        return (chr(ord(c)))


def uppercase(str):
    str1 = ""
    for character in str:
        str1 = is_lowerletter(character)
        print("{}".format(str1), end="")
    print(end="\n")
