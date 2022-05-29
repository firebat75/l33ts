def solution(s: str, target: str) -> int:

    s = list(s)
    target = list(target)

    x = True
    output = 0
    while x:
        for item in target:
            if item in s:
                s.remove(item)
            else:
                return output

        output += 1

print(solution(s = "abbaccaddaeea", target = "aaaaa"))