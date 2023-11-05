#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    arg_count = len(sys.argv) - 1
    sum = 0

    for i in range(1, arg_count + 1):
        num = int(sys.argv[i])
        if (num <= 0 or num >= 0):
            sum = sum + num
        else:
            continue
    print("{}".format(sum))
