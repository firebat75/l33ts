def solution(numRows):
    output = [[1]]
    for i in range(numRows-1):
        line = [1]
        for e in range(i):
            print(output, line, i, e)
            line.append(output[i][e] + output[i][e+1])
        line.append(1)
        output.append(line)
        
    return output

print(solution(5))
print(solution(1))