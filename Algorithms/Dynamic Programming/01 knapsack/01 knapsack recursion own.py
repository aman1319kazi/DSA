li = [0] 
def knapsack(n, w, val, wt, i = 0, total = 0, temp = 0): 
    if i >= n: 
        if total > li[0]: 
            li[0] = total 
        return 
     
    if temp+wt[i] <= w: 
        knapsack(n, w, val, wt, i+1, total+val[i], temp+wt[i]) 
     
    knapsack(n, w, val, wt, i+1, total, temp) 
     
n, w = 4, 4 
values = [5, 0, 1, 3] 
weights = [1, 1, 2, 3] 
knapsack(n, w, values, weights) 
print(li)