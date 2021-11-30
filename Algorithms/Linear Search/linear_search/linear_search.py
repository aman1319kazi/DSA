def Linear_search(arr, ele):
    index = -1
    for x in range(len(arr)):
        if arr[x] == ele:
            index = x
            break

    return index

print(Linear_search([1, 2, 2, 3, 4], 2))