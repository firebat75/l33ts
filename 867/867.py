class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        output = [[None] * len(matrix)] * len(matrix[0])
        output = [i[:] for i in output]

        for x in range(len(output)):
            for y in range(len(output[x])):
                output[x][y] = matrix[y][x]

        return output
