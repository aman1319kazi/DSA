n = int(input("total numbers? "))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a = a[:n+1]
b = b[:n+1]

print([a[i] * b[i] for i in range(n)])