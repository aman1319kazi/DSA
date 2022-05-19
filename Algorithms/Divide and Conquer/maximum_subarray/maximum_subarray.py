from max_crossing_subarray import max_crossing_subarray

def maximum_subarray(arr, low, high):
	if low >= high:
		return low, high, arr[low] 
	else:
		mid = (low + high) // 2
		print(arr[mid+1:])
		left_low, left_high, left_sum = maximum_subarray(arr, low, mid)
		right_low, right_high, right_sum = maximum_subarray(arr, mid+1, high)
		cross_low, cross_high, cross_sum = max_crossing_subarray(arr, low, mid, high)

		if left_sum >= right_sum and left_sum >= cross_sum:
			return left_low, left_high, left_sum

		elif right_sum >= left_sum and right_sum >= cross_sum:
			return right_low, right_high, right_sum

		else:
			return cross_low, cross_high, cross_sum

# arr = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4,7]
arr = [13, -3, -25, 20, -3]
low, high, sum = maximum_subarray(arr, 0, len(arr)-1)
print(low, high, sum)