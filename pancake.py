def pancakeSort(a):
    n = len(a)
    
    for size in range(n, 1, -1):
        maximum = a.index(max(a[:size]))

        if maximum!= 0:
            a[:maximum + 1] = reversed(a[:maximum + 1])
        
        a[:size] = reversed(a[:size])
    return a

a = [9, 3, 2, 5]
print(a)
pancakeSort(a)
print(a)