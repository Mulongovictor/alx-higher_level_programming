#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    idx_count = len(my_list)
    new_list = my_list.copy()
    if idx < 0:
        return (new_list)
    elif idx > idx_count - 1:
        return (new_list)
    else:
        for idx in range(idx_count - 1):
            new_list[idx] = element
            return (new_list)
