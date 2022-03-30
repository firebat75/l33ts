def solution(s):
    def backtrack(temp="", i=0):
        if len(temp) == len(s):
            output.append(temp)
        else:
            if s[i].isalpha():
                backtrack(temp + s[i].swapcase(), i + 1)
            backtrack(temp + s[i], i + 1)

    output = []
    backtrack()
    return output


print(solution("a1b2"))
print(solution("3z4"))
