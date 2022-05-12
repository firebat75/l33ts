def solution(n):

    # if n == 1:
    #     return 5

    # output = 5

    # for i in range(1, n):
    #     print(f"i: {i}")
    #     count = 1
    #     max = 1
    #     for e in range(1, output):
    #         output += count
    #         print(max, count, output)
    #         count += 1
    #         if count > max:
    #             max += 1
    #             count = 1
            
        


    # return output

    dp = [[0] * 6 for _ in range(n+1)]
    for i in range(1, 6):
        dp[1][i] = i
    
    for i in range(2, n+1):
        dp[i][1]=1
        for j in range(2, 6):
            dp[i][j] = dp[i][j-1] + dp[i-1][j]
    
    return dp[n][5]