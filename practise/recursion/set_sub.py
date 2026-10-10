def genSubsets(L):
    res = []
    if len(L) == 0:
        return [[]]
    smaller = genSubsets(L[:-1])
    extra = L[-1:]
    new = []
    for small in smaller:
        new.append(small+extra)
    return smaller+new


ans = 0
for i in range(5): 
    for j in range(5): 
        ans += 1 
        ans += 1 
print('Number of additions so far', ans) 