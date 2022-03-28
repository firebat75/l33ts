def solution(matrix):
    # output = []

    # width = len(matrix[0])
    # height = len(matrix)

    # x = 0
    # y = 0
    # rep = 0

    # state = 1

    # for i in range(width * height):

    #     output.append(matrix[y][x])

    #     if x == width - 1 - rep:
    #         if y == 0 - rep:  # top right
    #             state = 2
    #         elif y == height - 1 - rep:  # bottom right
    #             state = 3

    #     elif x == 0 + rep:
    #         if y == height - 1 - rep:  # bottom left
    #             state = 4
    #         elif y == 1 + rep:  # top left
    #             state = 1
    #             rep += 1

    #     if state == 1:
    #         x += 1
    #     elif state == 2:
    #         y += 1
    #     elif state == 3:
    #         x -= 1
    #     elif state == 4:
    #         y -= 1

    #     print("state:", state, " - reps:", rep)
    #     print(x, y)

    #     print(output)

    # return output
    res = []
    if len(matrix) == 0:
        return res
    row_begin = 0
    col_begin = 0
    row_end = len(matrix) - 1
    col_end = len(matrix[0]) - 1
    while row_begin <= row_end and col_begin <= col_end:
        for i in range(col_begin, col_end + 1):
            res.append(matrix[row_begin][i])
        row_begin += 1
        for i in range(row_begin, row_end + 1):
            res.append(matrix[i][col_end])
        col_end -= 1
        if row_begin <= row_end:
            for i in range(col_end, col_begin - 1, -1):
                res.append(matrix[row_end][i])
            row_end -= 1
        if col_begin <= col_end:
            for i in range(row_end, row_begin - 1, -1):
                res.append(matrix[i][col_begin])
            col_begin += 1
    return res


print(solution([[1]]))
print(solution([[1, 2], [3, 4]]))
print(solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(solution([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
print(
    solution(
        [
            [0, 1, 2, 3, 4],
            [5, 6, 7, 8, 9],
            [10, 11, 12, 13, 14],
            [15, 16, 17, 18, 19],
            [20, 21, 22, 23, 24],
        ]
    )
)
