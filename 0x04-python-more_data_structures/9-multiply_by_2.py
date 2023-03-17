#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    temp_dic = a_dictionary.copy()
    for i in temp_dic.keys():
        temp_dic[i] *= 2
    return temp_dic
