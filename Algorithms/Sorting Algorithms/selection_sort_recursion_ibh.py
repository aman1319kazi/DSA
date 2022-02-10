def find_max(arr, i):
	if i == 0:
		return 0

	j = find_max(arr, i - 1)
	if arr[j] > arr[i]:
		return j
	return i

def selection_sort(arr, i = None):
	if i is None:
		i = len(arr) - 1

	if i <= 0:
		return i

	pos = find_max(arr, i)
	arr[i], arr[pos] = arr[pos], arr[i]
	selection_sort(arr, i - 1)

arr = [5, 4, 3, 2, 1]
selection_sort(arr)
print(arr)