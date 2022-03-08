def bestSum(targetSum, numbers, memo = {}):
    if targetSum in memo:
        return memo[targetSum]

    if targetSum < 0:
        return None

    if targetSum == 0:
        return []

    best_sum_combination = None
    for num in numbers:
        target = targetSum - num
        ans = bestSum(target, numbers, memo)

        if ans is not None:
            ans = [num] + ans
            if best_sum_combination is None or len(ans) < len(best_sum_combination):
                best_sum_combination = ans

    memo[targetSum] = best_sum_combination
    return best_sum_combination

print(bestSum(7, [5, 3, 4, 7], {})) #[7]
print(bestSum(8, [2, 3, 5], {})) #[3, 5] 
print(bestSum(8, [1, 4, 5], {})) #[4, 4]
print(bestSum(100, [1, 2, 5, 25], {})) #[25, 25, 25, 25]