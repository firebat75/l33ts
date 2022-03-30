from pandas import *


def solution(board, word):

    HEIGHT = len(board) - 1
    WIDTH = len(board[0]) - 1

    def scan(b, x, y, target):  # returns tuple of directions to target
        check = [(0, -1), (-1, 0), (1, 0), (0, 1)]

        for t in check:
            if (
                0 <= x + t[0] <= WIDTH and 0 <= y + t[1] <= HEIGHT
            ):  # if checkspot index in range
                if b[y + t[1]][x + t[0]] == target:  # if checkspot is target
                    return t
        return None

    def check(a=[]):
        if scan() == None:
            return None

        elif scan():
            a.append(scan())

    for i in range(HEIGHT + 1):
        for e in range(WIDTH + 1):

            temp = []
            for line in board:
                temp.append(line.copy())
            f = []
            cx = e
            cy = i
            wind = 0

            print(cx, cy)
            print(word[wind], temp[cy][cx])
            print(f)
            print(DataFrame(temp))

            if temp[cy][cx] == word[wind]:
                wind += 1
                f.append(temp[cy][cx])
                temp[cy][cx] = ""

                print("FIRST")
                print(cx, cy)
                print(f)
                print(DataFrame(temp))

                while scan(temp, cx, cy, word[wind]):
                    direct = scan(temp, cx, cy, word[wind])

                    f.append(temp[cy + direct[1]][cx + direct[0]])
                    wind += 1
                    temp[cy + direct[1]][cx + direct[0]] = ""
                    cx += direct[0]
                    cy += direct[1]
                    if f == list(word):
                        return True

                    print("SCANNED")
                    print(cx, cy)
                    print(f)
                    print(DataFrame(temp))
            print("dropped")

    return False


print(
    solution(
        [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED"
    )
)
print(
    solution([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "SEE")
)
print(
    solution([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCB")
)
