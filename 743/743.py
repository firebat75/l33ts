def solution(times, n, k):

    nodes = {}

    for i in range(1, n + 1):
        nodes[i] = [False, 0]

    nodes[k][0] = True
    output = 0

    index = 0


    while index <= len(times):
        if nodes[times[index]][0] == True:
            

        else:
            index += 1


    while times:
        if nodes[times[index]][0] == True:
            if nodes[times[index + 1]][0] == True:
                nodes[times[index + 1]][1] = min(nodes[times[index+1]][1] , nodes[times[index]][1] + times[index][2])
            else:
                nodes[times[1]][0] = True
                nodes[times[1]][1] += nodes[times[0]][1] + times[2]

        

        print(nodes)

    for node in nodes:
        print(nodes[node][0])
        if nodes[node][0] == False:
            return -1
        else:
            output = max(output, nodes[node][1])

    return output

# print(solution(times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2))
# print(solution(times = [[1,2,1]], n = 2, k = 1))
# print(solution(times = [[1,2,1]], n = 2, k = 2))
print(solution(times = [[1,2,1],[2,3,7],[1,3,4],[2,1,2]], n = 3, k = 2))