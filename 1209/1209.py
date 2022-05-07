def solution(s, k):
    pointer = 0

    while pointer < len(s):
        print(s, pointer)
        if s[pointer:pointer+k] == s[pointer] * k:
            s = s[:pointer] + s[pointer+k:]
            if len(s) > pointer >= 1 and s[pointer] == s[pointer-1]:
                pointer -= k
                if pointer < 0:
                    pointer = 0
        else:
            pointer += 1

    return s

print(solution(
"yfttttfbbbbnnnnffbgffffgbbbbgssssgthyyyy",4))