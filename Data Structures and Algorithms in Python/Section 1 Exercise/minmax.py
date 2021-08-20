def minmax(li):
	min = float("inf")
	max = float("-inf")

	for x in range(len(li)):
		if li[x]<min:min = li[x]
		if li[x]>max :max = li[x]
	return min, max

print(minmax([1,2,3,4,5,6,7,8,9,10]))