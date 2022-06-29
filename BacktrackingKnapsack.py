def frac_knapsack(n,size, profit,K):
    if K <= 0:
       return 0
    for i in range(0,i):
        if profit[i]/size[i]>profit[i-1]/size[i-1]:
            profit.append[i] and size.append[i]
    s = 0
    p = 0
    for i in range(n):
        if s + size[i] <= K:
            p += profit[i]
            s += size[i]
        else: 
            p += (K-s) * (profit[i]/size[i])
            s = K
            break
        return p
def Knapsack(i, size):
    if i > n or size <= 0:
        print(x)
        return
    if x[j] == 1:
        for j in range(0,i-1):
           p+=P[j]
    if x[j] == 1:
        for j in range(0,i-1):
           s+=S[j]
    if x[i] == 1:
        if s+size[i] <= K and (p + profit[i] + B) > MaxProfit:
            B = frac_Knapsack(n-(i+1), size[i+1:], profit[i+1:], T-size[i])
        if p+profit[i] > MaxProfit:
            MaxProfit=p+profit[i]
            x=solution
        Knapsack(i+1, T-size[i])
        if x[i] == 0:
            B = frac_Knapsack(n-(i+1), size[i+1:], profit[i+1:], T)
        if (p + B) > MaxProfit:
            Knapsack(i+1, T)
