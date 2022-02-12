def counting_sort(arr, k):
	ans = [0] * (k+1)

	for x in range(k+1):
		ans[x] = arr.count(x)

	for prefix in range(1, k+1):
		ans[prefix] = ans[prefix] + ans[prefix-1]

	B = [None] * len(arr)

	for x in range(len(arr)-1, -1, -1):
		B[ans[arr[x]]-1] = arr[x]
		ans[arr[x]] = ans[arr[x]] - 1
	print(B)

arr = [2, 5, 3, 0, 2, 3, 0, 3] #[0, 0, 2, 2, 3, 3, 3, 5]
k = 5
counting_sort(arr, k)