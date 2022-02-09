def find_max(arr, i = 0, maxi = float("-inf"), ind = -1): 
    if i == len(arr): 
        return ind 
    if arr[i] > maxi: 
        maxi = arr[i] 
        ind = i 
    return find_max(arr, i + 1, maxi, ind) 
 
def selection_sort(arr, ind): 
    if ind == 0: 
        return 
    maxi = find_max(arr[:ind + 1]) 
     
    arr[maxi], arr[ind] = arr[ind], arr[maxi] 
    selection_sort(arr, ind-1) 
  

arr = [5, 4, 3, 2, 1]                                                  

selection_sort(arr, len(arr) - 1)

print(arr)