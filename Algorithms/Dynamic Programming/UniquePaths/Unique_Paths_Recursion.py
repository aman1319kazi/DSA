def uniquePaths(m, n):
    if m == 1 and n == 1:
        return 1

    if m == 0 or n == 0:
        return 0

    return uniquePaths(m - 1, n) + uniquePaths(m, n - 1)

print(uniquePaths(3, 7))    
print(uniquePaths(3, 2))