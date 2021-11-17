def can_sum(target, arr, memo={}):
    if target in memo:
        return memo[target]
    if target < 0:
        return False
    if target == 0:
        return True

    else:
        for x in arr:
            new_target = target - x
            if can_sum(new_target, arr, memo):
                memo[target] = True
                return True
        memo[target] = False
        return False


print(can_sum(7, [2, 3], {}))
print(can_sum(7, [5, 3, 4, 7], {}))
print(can_sum(7, [2, 4], {}))
print(can_sum(8, [2, 3, 5], {}))
print(can_sum(300, [7, 14], {}))
