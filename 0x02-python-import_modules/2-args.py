#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    arg_count = len(sys.argv) - 1
    if (arg_count < 1):
        print("{} argument.".format(arg_count))
    elif (arg_count == 1):
        print("{} argument:".format(arg_count))
    else:
        print("{} arguments:".format(arg_count))

    for i in (arg_count):
        print("{}: {}".format(i + 1, arg + 1))
