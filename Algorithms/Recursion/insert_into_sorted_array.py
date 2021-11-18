def insert_into_sorted_array(arr, ele):
	if not len(arr) or arr[-1]<ele:
		arr.append(ele)

	else:
		temp = arr.pop()
		insert_into_sorted_array(arr, ele)
		arr.append(temp)


arr = [1, 2, 3, 5]
insert_into_sorted_array(arr, 4)
print(arr)