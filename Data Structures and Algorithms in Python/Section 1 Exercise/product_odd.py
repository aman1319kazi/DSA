def odd_product(li):
	if len(set([x for x in li if x%2 ])) > 1: 
		print(set([x for x in li if not x%2 ]))
		return True
	return False

print(odd_product([1,2,3,4,5]))

