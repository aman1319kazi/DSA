def max_crossing_subarray(arr, low, mid, high):
	left_sum = float("-infinity")
	left_ind = float("-infinity")
	sum = 0
	for x in range(mid, low-1, -1):
		sum += arr[x]
		if sum > left_sum:
			left_sum = sum
			left_ind = x

	summ = 0
	right_ind = float("-infinity")
	right_sum = float("-infinity")
	for x in range(mid+1, high+1):
		summ += arr[x]
		if summ > right_sum:
			right_sum = summ
			right_ind = x
	return left_ind, right_ind, left_sum+right_sum


# arr = [100,200,-1000,100,50,30,-60,10]
# left, right, sum = max_crossing_subarray(arr, 0,len(arr)//2,len(arr)-1)
# print(left, right, sum)
# print(arr[left:right+1])