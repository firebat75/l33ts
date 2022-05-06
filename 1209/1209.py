def solution(s, k):
    pointer = 0

    while pointer < len(s):
        print(s, pointer)
        if s[pointer:pointer+k] == s[pointer] * k:
            s = s[:pointer] + s[pointer+k:]
            pointer = 0
        else:
            pointer += 1

    return s

print(solution("deeedbbcccbdaa",3))