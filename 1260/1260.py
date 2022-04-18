def solution(grid, k):
    k = k % len(grid[0])
    return None


print(solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1))
print(solution([[3, 8, 1, 9], [19, 7, 2, 5], [4, 6, 11, 10], [12, 0, 21, 13]], 4))
print(solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 9))
