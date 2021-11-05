def merge_sort(arr, p, r):
	if p < r:
		mid = (p+r) // 2
		merge_sort(arr, p, mid)
		merge_sort(arr, mid+1, r)
		merge(arr, p, mid, r)

def merge(arr, p, q, r):
	arr1 = arr[p:q+1] + [float("inf")]
	arr2 = arr[q+1:r+1] + [float("inf")]
	
	i, j = 0, 0
	for x in range(p, r+1):
		if arr1[i]<=arr2[j]:
			arr[x] = arr1[i]
			i+=1
		else :
			arr[x] = arr2[j]
			j+=1



arr = [5, 4, 3, 2, 1]
merge_sort(arr, 0, len(arr)-1)
print(arr)
