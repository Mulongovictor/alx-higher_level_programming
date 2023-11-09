#!/usr/bin/python3
def max_integer(my_list=[]):
    ele_count = len(my_list)
    if ele_count == 0:
        return (None)
    big_num = my_list[0]
    for i in range(ele_count):
        if my_list[i] > big_num:
            big_num = my_list[i]
    return (big_num)
