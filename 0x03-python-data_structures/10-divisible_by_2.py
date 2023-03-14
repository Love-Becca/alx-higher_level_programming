#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    update_list = []

    for i in my_list:
        if i % 2 == 0:
            update_list.append(True)
        else:
            update_list.append(False)
    return (update_list)
