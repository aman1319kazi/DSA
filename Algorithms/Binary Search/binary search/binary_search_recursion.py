def search(arr, l, r, ele):
    if l <= r:
        mid = (l + r) // 2
        if arr[mid] == ele:
            return mid

        elif ele < arr[mid]:
            return search(arr, l, mid - 1, ele)

        elif ele > arr[mid]:
            return search(arr, mid + 1, r, ele)

    else:
        return -1

arr = [1, 2, 3, 4, 5, 6]
ele = 4
print(search(arr, 0, len(arr) - 1, ele))
