def best_sum(target, arr, memo={}):
    if target < 0:
        return None
    if target == 0:
        return []

    min_combination = None
    for x in arr:
        new_target = target - x
        combination = best_sum(new_target, arr)
        if combination is not None:
            temp = combination + [x]
            if min_combination is None or len(temp)<len(min_combination):
                min_combination = temp

    return min_combination
print(best_sum(7, [2, 3, 6, 7], {}))
print(best_sum(7, [5, 3, 4, 7], {}))
print(best_sum(7, [2, 4], {}))
print(best_sum(8, [2, 3, 5], {}))
print(best_sum(300, [7, 14], {}))