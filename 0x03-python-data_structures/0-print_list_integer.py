#!/usr/bin/python3
def print_list_integer(my_list=[]):
    for element in range(len(my_list)):
        format_print = "{:d}".format(my_list[element])
        print(format_print)
