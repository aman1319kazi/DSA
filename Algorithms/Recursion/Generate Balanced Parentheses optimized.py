def generate(n, m, ans = ""): 
    if n == 0 and m == 0: 
        print(ans) 
        return 
     
    if n == m and n != 0: 
        generate(n - 1, m, ans + "(") 
         
    if n == 0 and m > 0: 
        return generate(n, m - 1, ans + ")") 
     
    if n != m:     
        generate(n - 1, m, ans + "(") 
        generate(n, m - 1, ans + ")")