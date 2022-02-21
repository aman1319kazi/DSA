class Solution:
    def josephus(self,n,k):
        def find(k, arr, pos): 
           if len(arr) == 1:
              return arr[0] 
           pos = (pos + k) % len(arr) 
           arr.pop(pos) 
           return find(k, arr, pos)
    
        return find(k - 1, list(range(1, n + 1)), 0)