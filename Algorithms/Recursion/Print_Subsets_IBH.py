from copy import deepcopy
def print_subsets(arr):
    if not arr:
        return [[]]

    tempele = arr.pop()
    ans = print_subsets(arr)

    temparr = deepcopy(ans)
    for ele in range(len(temparr)):
        temparr[ele].append(tempele)
    return ans + temparr

print(print_subsets([1, 2, 3]))


'''
{1, 2} => {{}, {1}, {2}, {1, 2}}
{1, 2, 3} => {{}, {1}, {2}, {1, 2}, {3}, {1, 3}, {2, 3}, {1, 2, 3}}
'''

