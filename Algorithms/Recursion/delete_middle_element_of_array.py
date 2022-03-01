def delete_middle(arr, middle):
    if not arr:
        return

    if middle == 0:
        arr.pop()
        return

    temp = arr.pop()
    delete_middle(arr, middle-1)
    arr.append(temp)

arr = [1, 2, 3, 4, 5, 6]

delete_middle(arr, len(arr) // 2)
print(arr)