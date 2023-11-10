#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    list_len = len(my_list)

    for i in range(list_len - 1):
        if idx < 0:
            return (my_list)
        elif idx > list_len:
            return (my_list)
        else:
            if i == idx:
                del my_list[i]
    return (my_list)
