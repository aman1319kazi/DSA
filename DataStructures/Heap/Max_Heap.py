def parent(i):
    return (i - 1) // 2

def left_child(i):
    return (2 * i) + 1

def right_child(i):
    return (2 * i) + 2

def max_heapify(A, i, heapsize):
    l = left_child(i)
    r = right_child(i)

    if l < heapsize and A[l] > A[i]:
        largest = l
    else:
        largest = i

    if r < heapsize and A[r] > A[largest]:
        largest = r

    if largest != i:
        A[largest], A[i] = A[i], A[largest]
        max_heapify(A, largest, heapsize)

def build_maximum_heap(A, heap_size):
    for i in range((heap_size-1) // 2, -1, -1):
        max_heapify(A, i, heap_size)