def howSum(targetSum, numbers):
	if targetSum < 0:
		return None
	
	if targetSum == 0:
		return []

	for num in numbers:
		target = targetSum - num
		ans = howSum(target, numbers)
		if ans is not None:
			return [num] + ans
	return None

print(howSum(7, [2, 3, 6, 7]))
print(howSum(7, [5, 3, 4, 7]))
print(howSum(7, [2, 4]))
print(howSum(8, [2, 3, 5]))
print(howSum(300, [7, 14]))
