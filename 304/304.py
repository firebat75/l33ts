class NumMatrix:
    def __init__(self, matrix):
        self.matrix = matrix

        for row in range(len(self.matrix)):
            for col in range(1, len(self.matrix[row])):
                self.matrix[row][col] += self.matrix[row][col - 1]

        print(matrix)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        output = 0

        # for y in range(row1, row2 + 1):
        #     for x in range(col1, col2 + 1):
        #         output += self.matrix[y][x]

        # for y in range(row1, row2 + 1):
        #     output += sum(self.matrix[y][col1 : col2 + 1])

        for row in range(row1, row2 + 1):
            if col1 == 0:
                output += self.matrix[row][col2]
            else:
                output += self.matrix[row][col2] - self.matrix[row][col1 - 1]

        return output


matrix = [
    [3, 0, 1, 4, 2],
    [5, 6, 3, 2, 1],
    [1, 2, 0, 1, 5],
    [4, 1, 0, 1, 7],
    [1, 0, 3, 0, 5],
]
obj = NumMatrix(matrix)
param_1 = obj.sumRegion(2, 1, 4, 3)

print(param_1)


matrix = [[-4, -5]]
obj = NumMatrix(matrix)
param_1 = obj.sumRegion(0, 0, 0, 0)
param_2 = obj.sumRegion(0, 0, 0, 1)
param_3 = obj.sumRegion(0, 1, 0, 1)

print(param_1)
print(param_2)
print(param_3)
