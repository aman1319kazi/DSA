def uniquePaths(m, n):
    dp = [[0 for x in range(n + 1)] for y in range(m + 1)]
    dp[1][1] = 1

    for x in range(1, m + 1):
        for y in range(1, n + 1):
            if x != 1 or y != 1:
                dp[x][y] = dp[x - 1][y] + dp[x][y - 1]

    return dp[-1][-1]

print(uniquePaths(3, 7))    
print(uniquePaths(3, 2))