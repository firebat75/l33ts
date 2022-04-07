def solution(n):
    def backtracking(path, l, r):
        if (l, r) == (0, 0):
            output.append(path)

        if l > 0:
            backtracking(path + "(", l - 1, r)
        if r > l:
            backtracking(path + ")", l, r - 1)

    output = []
    backtracking("", n, n)
    return output


print(solution(3))
print(solution(1))
