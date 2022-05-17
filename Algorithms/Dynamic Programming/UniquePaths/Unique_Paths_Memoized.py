def uniquePaths(m, n, memo):
    if (m, n) in memo:
        return memo[(m, n)]

    if m == 1 and n == 1:
        return 1

    if m == 0 or n == 0:
        return 0

    memo[(m, n)] = uniquePaths(m - 1, n, memo) + uniquePaths(m, n - 1, memo)
    return memo[(m, n)]

print(uniquePaths(3, 7, {}))    
print(uniquePaths(3, 2, {}))