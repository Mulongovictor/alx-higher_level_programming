#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    idx_count = len(my_list)
    if idx < 0:
        return (my_list)
    elif idx > idx_count - 1:
        return (my_list)
    else:
        new_list = my_list.copy()
        new_list[idx] = element
        for idx in range(idx_count - 1):
            return (new_list)
