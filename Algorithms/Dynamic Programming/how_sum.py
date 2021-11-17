def how_sum(target, arr, memo = {}):
    if target in memo:
        return memo[target]
    if target < 0:
        return None
    if target == 0:
        return []

    else:
        for x in arr:
            new_target = target - x
            temp = how_sum(new_target, arr, memo)
            if temp is not None:
                memo[target] = [x] + temp
                return memo[target]

        memo[target] = None


print(how_sum(7, [2, 3, 6, 7], {}))
print(how_sum(7, [5, 3, 4, 7], {}))
print(how_sum(7, [2, 4], {}))
print(how_sum(8, [2, 3, 5], {}))
print(how_sum(300, [7, 14], {}))