#!/usr/bin/python3
def multiple_returns(sentence):
    t = ()
    length = len(sentence)
    if sentence == "":
        return (0, None)
    else:
        chara = sentence[0]
    t = length, chara
    return (t)
