def bubble_sort(arr):
    for x in range(len(arr)):
        not_swapped = True
        for y in range(0, len(arr) - x - 1):
            if arr[y] > arr[y + 1]:
                arr[y], arr[y + 1] = arr[y + 1], arr[y]
                not_swapped = False

        if not_swapped:
            break

arr = [1, 2, 3, 4, 5]
bubble_sort(arr)
print(arr)
