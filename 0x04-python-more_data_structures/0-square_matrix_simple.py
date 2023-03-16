#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    multiple_of_two = []
    for i in matrix:
        multiple_of_two.append(list(map(lambda i: i**2, i)))
    return (multiple_of_two)
