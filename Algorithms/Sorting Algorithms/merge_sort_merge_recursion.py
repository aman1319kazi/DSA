def merge(L, R, arr, l, r, a, b): 
    if b == -1: 
        return 
         
    if (r == -1 and l > -1) or (l > -1 and L[l] > R[r]): 
        arr[b] = L[l] 
        l = l - 1 
 
    elif (l==-1 and r > -1) or (r > -1 and R[r] > L[l]): 
        arr[b] = R[r] 
        r = r - 1 
         
    merge(L, R, arr, l, r, a, b - 1) 
 
def mergesort(arr): 
    if len(arr) > 1: 
        L = arr[:len(arr) // 2] 
        R = arr[len(arr) // 2:] 
        mergesort(L) 
        mergesort(R) 
        merge(L, R, arr, len(L) - 1, len(R) - 1, 0, len(arr) - 1) 
 
arr = [5, 4, 3, 2, 1] 
mergesort(arr) 
print(arr)