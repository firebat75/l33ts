from pandas import *


def solution(n):
    row = [1] * n
    grid = []
    for i in range(n):
        grid.append(row.copy())

    x = 0
    y = 0
    rep = 0
    dir = "right"
    for i in range(2, n ** 2 + 1):
        if dir == "right":
            x += 1
        elif dir == "down":
            y += 1
        elif dir == "left":
            x -= 1
        elif dir == "up":
            y -= 1

        grid[y][x] = i

        if x == n - rep - 1 and y == 0 + rep:  # top right
            dir = "down"
        elif x == n - rep - 1 and y == n - rep - 1:  # bottom right
            dir = "left"
        elif x == 0 + rep and y == n - rep - 1:  # bottom left
            dir = "up"
        elif x == 0 + rep and y == 1 + rep:  # top left
            rep += 1
            dir = "right"

    return grid


print(solution(1))
print(solution(2))
print(solution(3))
print(solution(4))
print(solution(5))
