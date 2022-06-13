class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        triangle.reverse()
        
        for row in range(1, len(triangle)):
            for i in range(len(triangle[row])):
                triangle[row][i] += min(triangle[row-1][i], triangle[row-1][i+1])

        return triangle[-1][0]