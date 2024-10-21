def shellSort(a):
    n = len(a)
    gap = n//2

    while gap > 0:
        for i in range(gap, n):
            temp = a[i]
            j = i
            while j >= gap and a[j - gap] > temp:
                a[j] = a[j - gap]
                j -= gap
        
            a[j] = temp

        gap //= 2
        
a = [9, 3, 2, 5]
print(a)
shellSort(a)
print(a)
