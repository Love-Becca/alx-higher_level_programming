#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    update_list = []

    for i in my_list:
        if i % 2 == 0:
            update_list.append(True)
        else:
            update_list.append(False)
    return (update_list)
