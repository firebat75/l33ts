def solution(ops):
    output = []
    for i in range(len(ops)):
        print(output)
        print(ops[i])
        if ops[i].isdigit() or ops[i][0] == "-":
            output.append(int(ops[i]))
        elif ops[i] == "+":
            output.append(output[-1] + output[-2])
        elif ops[i] == "D":
            output.append(output[-1] * 2)
        elif ops[i] == "C":
            output = output[:-1]
    print(output)
    return sum(output)


# print(solution(["5", "2", "C", "D", "+"]))
# print(solution(["5", "-2", "4", "C", "D", "9", "+", "+"]))
print(solution(["5", "-2", "4", "C", "D", "9", "+", "+"]))
