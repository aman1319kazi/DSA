def bestSum(targetSum, numbers):
	if targetSum < 0:
		return None

	if targetSum == 0:
		return []

	bestSumCombination = None

	for num in numbers:
		target = targetSum - num
		ans = bestSum(target, numbers)
		if ans is not None:
			ans = [num] + ans
			if bestSumCombination is None or len(bestSumCombination) > len(ans):
				bestSumCombination = ans

	return bestSumCombination

print(bestSum(7, [5, 3, 4, 7])) #[7]
print(bestSum(8, [2, 3, 5])) #[3, 5] 
print(bestSum(8, [1, 4, 5])) #[4, 4]
print(bestSum(100, [1, 2, 5, 25])) #[25, 25, 25, 25]

