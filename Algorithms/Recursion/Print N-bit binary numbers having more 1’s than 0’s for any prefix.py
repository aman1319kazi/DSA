li = []
def noofones(n, zeros, ones, ans = ""): 
    if zeros + ones == n: 
        li.append(ans)
        return li
         
    if zeros == ones: 
        ans += "1" 
        noofones(n, zeros, ones - 1, ans)
        return li 
    else: 
        op1 = ans + "0" 
        op2 = ans + "1" 
        noofones(n, zeros, ones - 1, op2)
        noofones(n, zeros - 1, ones, op1)
        return li

print(noofones(3, 3, 3))