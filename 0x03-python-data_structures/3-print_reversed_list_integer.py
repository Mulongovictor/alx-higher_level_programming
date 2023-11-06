#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if isinstance(my_list, list):
        list_len = len(my_list)
        my_list.reverse()
        for i in range(list_len):
            print("{}".format(my_list[i]))
