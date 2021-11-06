def merge_sort(arr):
	if len(arr)>1:
		mid = len(arr) // 2
		left_array = arr[:mid]
		right_array = arr[mid:]

		merge_sort(left_array)
		merge_sort(right_array)
		merge(left_array, right_array, arr)

def merge(larray, rarray, arr):
	i = j = 0
	larray.append(float("inf"))
	rarray.append(float("inf"))
	for x in range(len(arr)):
		if larray[i] <= rarray[j]:
			arr[x] = larray[i]
			i+=1
		else:
			arr[x] = rarray[j]
			j+=1

arr = [0, 0, 1, 2, 50, 1, 10]
merge_sort(arr)
print(arr)

