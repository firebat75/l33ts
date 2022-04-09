def solution(s):
    def backtracking(path, s):
        print(path, s, output)
        if not s:
            output.append(path)
        for i in range(1, len(s) + 1):
            if s[:i] == s[:i][::-1]:  # if s is palindrome
                backtracking(path + [s[:i]], s[i:])

    output = []
    backtracking([], s)

    return output


print(solution("aab"))
print(solution("a"))
