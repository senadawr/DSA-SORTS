def selectionSort(a):
    n = len(a)
    for i in range(n - 1):
        min = 1
    
        for j in range(i + 1, n):
            if a[j] < a[min]:
                min = j
    
        a[i], a[min] = a[min], a[i]

a = [9, 3, 2, 5]
print(a)
selectionSort(a)
print(a)