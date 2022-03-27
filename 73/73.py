def solution(matrix):

    rows = []
    cols = []

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == 0:
                if row not in rows:
                    rows.append(row)
                if col not in cols:
                    cols.append(col)

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if row in rows or col in cols:
                print(row, col)
                matrix[row][col] = 0

    print(rows, cols)
    # return matrix


print(solution([[1, 1, 1], [1, 0, 1], [1, 1, 1]]))
print(solution([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]))
