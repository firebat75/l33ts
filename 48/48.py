import pandas
from pandas import *


def solution(matrix):
    print("Original")
    print(DataFrame(matrix))
    matrix.reverse()
    print("Reversed")
    print(DataFrame(matrix))
    for i in range(len(matrix)):
        for e in range(i):
            matrix[i][e], matrix[e][i] = matrix[e][i], matrix[i][e]
            print("curr")
            print(i, e)
            print(DataFrame(matrix))


print(solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(solution([[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]))
