def solution(rowIndex):
    output = [[1]]
    for i in range(rowIndex):
        line = [1]
        for e in range(i):
            line.append(output[i][e] + output[i][e+1])
        line.append(1)
        output.append(line)
        
    return output[-1]

print(solution(3))
print(solution(1))