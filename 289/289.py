def solution(board):
    def isvalid(y, x):
        if 0 <= y <= len(board) - 1 and 0 <= x <= len(board[0]) - 1:
            return True
        return False

    def check(y, x):
        live = [1, 4, 5]

        val = board[y][x]

        output = 0

        if isvalid(y - 1, x - 1):  # up-left
            if board[y - 1][x - 1] in live:
                output += 1
        if isvalid(y - 1, x):  # up
            if board[y - 1][x] in live:
                output += 1
        if isvalid(y - 1, x + 1):  # up-right
            if board[y - 1][x + 1] in live:
                output += 1
        if isvalid(y, x - 1):  # left
            if board[y][x - 1] in live:
                output += 1
        if isvalid(y, x + 1):  # right
            if board[y][x + 1] in live:
                output += 1
        if isvalid(y + 1, x - 1):  # down-left
            if board[y + 1][x - 1] in live:
                output += 1
        if isvalid(y + 1, x):  # down
            if board[y + 1][x] in live:
                output += 1
        if isvalid(y + 1, x + 1):  # down-right
            if board[y + 1][x + 1] in live:
                output += 1

        if val == 0:
            if output == 3:
                return 3
            else:
                return 2
        elif val == 1:
            if output < 2 or output > 3:
                return 4
            else:
                return 5

    for r in range(len(board)):
        for c in range(len(board[0])):

            board[r][c] = check(r, c)

    dead = [2, 4]

    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] in dead:
                board[r][c] = 0
            else:
                board[r][c] = 1


print(solution([[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]))
print(solution([[1, 1], [1, 0]]))
