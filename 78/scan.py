from pandas import *

BOARD = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
HEIGHT = len(BOARD) - 1
WIDTH = len(BOARD[0]) - 1


def scan(b, x, y, target):  # returns tuple of directions to target
    check = [(0, -1), (-1, 0), (1, 0), (0, 1)]

    for t in check:
        print(f"0 <= {x + t[0]} <= WIDTH, 0 <= {y + t[1]} <= HEIGHT")
        print(0 <= x + t[0] <= WIDTH, 0 <= y + t[1] <= HEIGHT)
        print(target, b[y + t[1]][x + t[0]])
        print("----------------------")
        if (
            0 <= x + t[0] <= WIDTH and 0 <= y + t[1] <= HEIGHT
        ):  # if checkspot index in range
            if b[y + t[1]][x + t[0]] == target:  # if checkspot is target
                return t
    return False
