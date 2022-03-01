def canSum(targetSum, numbers, memo = {}):
    if targetSum in memo:
        return memo[targetSum]

    if targetSum < 0: 
        return False 
         
    if targetSum == 0: 
        return True 
     
    for num in numbers: 
        target = targetSum - num 
        if canSum(target, numbers, memo): 
            memo[targetSum] = True
            return True 

    memo[targetSum] = False
    return False

print(canSum(7, [2, 3], {}))
print(canSum(7, [5, 3, 4, 7], {}))
print(canSum(7, [2, 4], {}))
print(canSum(8, [2, 3, 5], {}))
print(canSum(300, [7, 14], {}))