def bubble_sort(arr):
    for x in range(len(arr)):
        for y in range(0, len(arr) - x - 1):
            if arr[y] > arr[y + 1]:
                arr[y], arr[y + 1] = arr[y + 1], arr[y]
        print(arr)
arr = [5, 1, 4, 2, 8]
bubble_sort(arr)
print(arr)
