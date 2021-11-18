def sorting_using_recursion(arr):
    if not len(arr):
        return
    else:
        temp = arr.pop()
        sorting_using_recursion(arr)
        insert_into_sorted_array(arr, temp)

def insert_into_sorted_array(arr, ele):
        if not len(arr) or arr[-1]<ele:
                arr.append(ele)

        else:
                temp = arr.pop()
                insert_into_sorted_array(arr, ele)
                arr.append(temp)

arr = [5, 4, -3, 2, 1]
sorting_using_recursion(arr)
print(arr)