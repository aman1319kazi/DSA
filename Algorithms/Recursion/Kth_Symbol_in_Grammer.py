def Kth_Symbol_in_Grammer(n, k):
    mid = 2**(n - 2)
    
    if n == 1 or k == 1:
        return 0

    if k <= mid:
        return Kth_Symbol_in_Grammer(n - 1, k)
    
    return 1 - Kth_Symbol_in_Grammer(n - 1, k - mid)

n, k = 3, 3
print(Kth_Symbol_in_Grammer(n, k))