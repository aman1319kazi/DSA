def insertion_sort_for_loop(arr):
    for x in range(1, len(arr)):
        key = arr[x]

        for y in range(x - 1, -2, -1):
            if arr[y] > key:
                arr[y + 1] = arr[y]

            else:
                break

        arr[y + 1] = key

li = [1, 2, 3, 4, 5]
insertion_sort_for_loop(li)
print(li)
