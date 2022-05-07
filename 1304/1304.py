def solution(n):

    output = []

    for i in range(1, (n//2)+1):
        output.append(i)
        output.append(i*-1)

    if n%2:
        output.append(0)

    return output

print(solution(8))
print(solution(2))
print(solution(1))