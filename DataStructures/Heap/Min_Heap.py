def parent(i):
    return (i - 1) // 2

def left_child(i):
    return (2 * i) + 1

def right_child(i):
    return (2 * i) + 2

def min_heapify(A, i, heapsize):
    l = left_child(i)
    r = right_child(i)

    if l < heapsize and A[l] < A[i]:
        smallest = l
    else:
        smallest = i

    if r < heapsize and A[r] < A[smallest]:
        smallest = r

    if smallest != i:
        A[smallest], A[i] = A[i], A[smallest]
        min_heapify(A, smallest, heapsize)


def build_minimum_heap(A, heap_size):
    for i in range((heap_size-1) // 2, -1, -1):
        min_heapify(A, i, heap_size)
