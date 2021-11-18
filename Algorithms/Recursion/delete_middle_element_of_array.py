def delete_middle(arr, middle):
	if not arr:
		return

	if middle == 0:
		arr.pop()
		return 
		
	temp = arr.pop()
	delete_middle(arr, middle-1)
	arr.append(temp)

arr = [6, 5, 4, 3, 2, 1]
delete_middle(arr, len(arr)//2)
print(arr)